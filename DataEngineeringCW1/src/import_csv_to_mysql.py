"""Fallback importer for environments where LOAD DATA LOCAL INFILE is blocked.

Usage:
    python src/import_csv_to_mysql.py

Update credentials below if needed.
"""

from __future__ import annotations

from pathlib import Path

import mysql.connector
import pandas as pd


CSV_PATH = Path("data/techreads_books.csv")

MYSQL_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",  # set your password if required
    "database": "techreads_db",
}


def main() -> None:
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)
    rows = [
        (
            r.get("title"),
            r.get("author"),
            int(r["publication_year"]) if pd.notna(r.get("publication_year")) else None,
            float(r.get("price_gbp", 0)),
            int(r.get("rating", 0)),
            r.get("availability"),
            r.get("product_url"),
            r.get("scraped_at_utc"),
        )
        for _, r in df.iterrows()
    ]

    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cur = conn.cursor()

    cur.execute("DELETE FROM techreads_books")
    insert_sql = """
        INSERT INTO techreads_books
        (title, author, publication_year, price_gbp, rating, availability, product_url, scraped_at_utc)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.executemany(insert_sql, rows)
    conn.commit()

    print(f"Inserted {cur.rowcount} rows into techreads_db.techreads_books")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
