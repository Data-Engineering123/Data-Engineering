"""Convert scraped CSV to JSON for MongoDB insertion (Task 4)."""

from pathlib import Path
import pandas as pd


INPUT_CSV = Path("data/techreads_books.csv")
OUTPUT_JSON = Path("data/techreads_books.json")


def main() -> None:
    if not INPUT_CSV.exists():
        raise FileNotFoundError(f"Input CSV not found: {INPUT_CSV}")

    df = pd.read_csv(INPUT_CSV)

    # Ensure numeric fields are clean
    if "price_gbp" in df.columns:
        df["price_gbp"] = pd.to_numeric(df["price_gbp"], errors="coerce")
    if "rating" in df.columns:
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    df.to_json(OUTPUT_JSON, orient="records", indent=2, force_ascii=False)
    print(f"Created JSON file: {OUTPUT_JSON} ({len(df)} records)")


if __name__ == "__main__":
    main()
