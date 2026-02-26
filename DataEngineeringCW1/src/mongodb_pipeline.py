"""Task 4: Insert JSON into MongoDB and run filter queries."""

from __future__ import annotations

import json
import time
from pathlib import Path

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "techreads_mongo_db"
COLLECTION_NAME = "books"
INPUT_JSON = Path("data/techreads_books.json")


def main() -> None:
    if not INPUT_JSON.exists():
        raise FileNotFoundError(f"JSON input not found: {INPUT_JSON}")

    data = json.loads(INPUT_JSON.read_text(encoding="utf-8"))
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    try:
        client.admin.command("ping")
    except ServerSelectionTimeoutError as exc:
        raise RuntimeError(
            "MongoDB is not running or not reachable at mongodb://localhost:27017/. "
            "Start MongoDB service (or mongod) and run this script again."
        ) from exc

    col = client[DB_NAME][COLLECTION_NAME]

    # Fresh load for repeatable demos
    col.delete_many({})
    if data:
        col.insert_many(data)

    print(f"Inserted {len(data)} documents into {DB_NAME}.{COLLECTION_NAME}")

    # Example query as required by brief (price/rating/year style filters)
    query = {
        "price_gbp": {"$lt": 40},
        "rating": {"$gte": 4},
    }
    projection = {"_id": 0, "title": 1, "price_gbp": 1, "rating": 1}

    start = time.perf_counter()
    results = list(col.find(query, projection).sort([("rating", -1), ("price_gbp", 1)]))
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"Mongo query returned {len(results)} records in {elapsed_ms:.3f} ms")
    for row in results[:5]:
        print(row)

    # Add index and rerun for comparison
    col.create_index([("rating", -1), ("price_gbp", 1)])
    start_idx = time.perf_counter()
    _ = list(col.find(query, projection).sort([("rating", -1), ("price_gbp", 1)]))
    elapsed_idx_ms = (time.perf_counter() - start_idx) * 1000
    print(f"Mongo query with index: {elapsed_idx_ms:.3f} ms")


if __name__ == "__main__":
    main()
