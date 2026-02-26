"""
Task 1: Web scraping for TechReads CW1.

Scrapes Data Engineering related books from books.toscrape.com
using requests + BeautifulSoup, structures with pandas, and
saves output to data/techreads_books.csv.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Dict, List
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = urljoin(BASE_URL, "catalogue/")
OUTPUT_CSV = Path("data/techreads_books.csv")


RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def fetch_html(url: str) -> str:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    # Force UTF-8 decode to avoid Windows codepage artifacts like 'Â51.77'
    return response.content.decode("utf-8", errors="replace")


def parse_book_card(book_article, scraped_at: str) -> Dict[str, object]:
    title_tag = book_article.select_one("h3 a")
    title = title_tag.get("title", "").strip()
    relative_url = title_tag.get("href", "")
    product_url = urljoin(CATALOGUE_URL, relative_url)

    price_text = book_article.select_one("p.price_color").get_text(strip=True)
    # Robust numeric extraction to handle encoding artifacts e.g. 'Â51.77'
    price_match = re.search(r"\d+(?:\.\d+)?", price_text)
    if not price_match:
        raise ValueError(f"Could not parse price from text: {price_text}")
    price_gbp = float(price_match.group(0))

    rating_classes = book_article.select_one("p.star-rating").get("class", [])
    rating_word = next((c for c in rating_classes if c in RATING_MAP), "One")
    rating = RATING_MAP[rating_word]

    availability_text = book_article.select_one("p.instock.availability").get_text(" ", strip=True)

    return {
        "title": title,
        "author": "Unknown",
        "publication_year": None,
        "price_gbp": price_gbp,
        "rating": rating,
        "availability": availability_text,
        "product_url": product_url,
        "scraped_at_utc": scraped_at,
    }


def scrape_books(min_books: int = 15, max_pages: int = 8) -> List[Dict[str, object]]:
    books: List[Dict[str, object]] = []
    scraped_at = datetime.now(timezone.utc).isoformat()

    for page in range(1, max_pages + 1):
        page_url = urljoin(CATALOGUE_URL, f"page-{page}.html")
        html = fetch_html(page_url)
        soup = BeautifulSoup(html, "html.parser")
        cards = soup.select("article.product_pod")

        for card in cards:
            books.append(parse_book_card(card, scraped_at))
            if len(books) >= min_books:
                return books

    return books


def main() -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    records = scrape_books(min_books=15, max_pages=8)
    if len(records) < 15:
        raise RuntimeError(f"Only scraped {len(records)} records; expected at least 15.")

    df = pd.DataFrame(records)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")

    print(f"Saved {len(df)} records to {OUTPUT_CSV}")
    print(df.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
