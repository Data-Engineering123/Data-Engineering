"""
Task 1: Web scraping for TechReads CW1.

Scrapes Data Engineering related books from
https://www.packtpub.com/en-gb/data/concept/data-engineering
using requests + BeautifulSoup, structures with pandas, and
saves output to data/techreads_books.csv.
"""

from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup


LISTING_URL = "https://www.packtpub.com/en-gb/data/concept/data-engineering"
OUTPUT_CSV = Path("data/techreads_books.csv")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def fetch_html(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.content.decode("utf-8", errors="replace")


def parse_rating(rating_text: str) -> Optional[float]:
    """Parse '4.7 (57)' -> 4.7"""
    match = re.search(r"(\d+\.\d+|\d+)", rating_text)
    return float(match.group(1)) if match else None


def parse_price(price_text: str) -> Optional[float]:
    """Extract numeric price from text, robust to encoding artefacts."""
    match = re.search(r"\d+(?:\.\d+)?", price_text)
    return float(match.group(0)) if match else None


def parse_pub_year(date_text: str) -> Optional[int]:
    """Parse 'Mar 2024' -> 2024"""
    match = re.search(r"\b(20\d{2})\b", date_text)
    return int(match.group(1)) if match else None


def fetch_author(product_url: str) -> str:
    """Fetch individual product page and extract author name(s)."""
    try:
        html = fetch_html(product_url)
        soup = BeautifulSoup(html, "html.parser")
        authors_div = soup.select_one("div.authors")
        if authors_div:
            names = [
                span.get_text(" ", strip=True)
                for span in authors_div.select("span.authors-dark")
                if span.get_text(strip=True)
            ]
            if names:
                return ", ".join(names)
    except Exception:
        pass
    return "Unknown"


def parse_card(card, scraped_at: str) -> Optional[Dict[str, object]]:
    # Title
    title_el = card.select_one(".ellipsis")
    title = title_el.get_text(strip=True) if title_el else ""
    if not title:
        return None

    # Product URL
    link_el = card.select_one("a.product-card-content-info")
    if not link_el:
        return None
    product_url = link_el.get("href", "")

    # Publication date (first device-fc-black-2 span in the meta block)
    meta_block = card.select_one("div.product-meta")
    publication_year = None
    if meta_block:
        date_span = meta_block.select_one("span.device-fc-black-2")
        if date_span:
            publication_year = parse_pub_year(date_span.get_text(strip=True))

    # Rating
    rating_el = card.select_one(".star-rating-total-rating-medium")
    rating = parse_rating(rating_el.get_text(strip=True)) if rating_el else None

    # eBook price (first .item-price element)
    price_el = card.select_one(".item-price")
    price_gbp = parse_price(price_el.get_text(strip=True)) if price_el else None

    return {
        "title": title,
        "author": None,  # populated after product page fetch
        "publication_year": publication_year,
        "price_gbp": price_gbp,
        "rating": rating,
        "availability": "In stock",
        "product_url": product_url,
        "scraped_at_utc": scraped_at,
    }


def scrape_books(min_books: int = 15) -> List[Dict[str, object]]:
    scraped_at = datetime.now(timezone.utc).isoformat()
    html = fetch_html(LISTING_URL)
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("div.product-card-content")
    records: List[Dict[str, object]] = []

    for card in cards:
        rec = parse_card(card, scraped_at)
        if rec:
            records.append(rec)
        if len(records) >= min_books:
            break

    if len(records) < min_books:
        raise RuntimeError(
            f"Only found {len(records)} cards on listing page; expected at least {min_books}."
        )

    # Fetch author from each product page (polite 0.5 s delay)
    print(f"Fetching author data from {len(records)} product pages...")
    for i, rec in enumerate(records, 1):
        rec["author"] = fetch_author(rec["product_url"])
        print(f"  [{i}/{len(records)}] {rec['title']} — {rec['author']}")
        time.sleep(0.5)

    return records


def main() -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    records = scrape_books(min_books=15)

    df = pd.DataFrame(records)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")

    print(f"\nSaved {len(df)} records to {OUTPUT_CSV}")
    print(
        df[["title", "author", "publication_year", "price_gbp", "rating"]]
        .head(5)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
