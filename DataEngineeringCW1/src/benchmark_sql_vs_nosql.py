"""Task 4: Compare similar query execution time in MySQL vs MongoDB."""

from __future__ import annotations

import os
import time

import mysql.connector
from pymongo import MongoClient
from mysql.connector import Error as MySQLError


# Adjust credentials for your local setup.
# You can also set environment variables:
# MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "techreads_db"),
}

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "techreads_mongo_db"
MONGO_COLLECTION = "books"


def benchmark_mysql() -> float:
    query = """
        SELECT title, price_gbp, rating
        FROM techreads_books
        WHERE rating >= 4 AND price_gbp < 40
        ORDER BY rating DESC, price_gbp ASC
    """

    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cur = conn.cursor()

    start = time.perf_counter()
    cur.execute(query)
    _ = cur.fetchall()
    elapsed_ms = (time.perf_counter() - start) * 1000

    cur.close()
    conn.close()
    return elapsed_ms


def benchmark_mongodb() -> float:
    client = MongoClient(MONGO_URI)
    col = client[MONGO_DB][MONGO_COLLECTION]

    query = {
        "rating": {"$gte": 4},
        "price_gbp": {"$lt": 40},
    }

    start = time.perf_counter()
    _ = list(
        col.find(query, {"_id": 0, "title": 1, "price_gbp": 1, "rating": 1}).sort(
            [("rating", -1), ("price_gbp", 1)]
        )
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    return elapsed_ms


def main() -> None:
    try:
        mysql_ms = benchmark_mysql()
    except MySQLError as exc:
        raise RuntimeError(
            "MySQL connection failed. Update credentials in src/benchmark_sql_vs_nosql.py "
            "or set env vars MYSQL_USER and MYSQL_PASSWORD before running."
        ) from exc
    mongo_ms = benchmark_mongodb()

    print("=== SQL vs NoSQL Query Time Comparison ===")
    print(f"MySQL query time   : {mysql_ms:.3f} ms")
    print(f"MongoDB query time : {mongo_ms:.3f} ms")

    if mysql_ms < mongo_ms:
        print("Observation: MySQL was faster in this local test run.")
    elif mongo_ms < mysql_ms:
        print("Observation: MongoDB was faster in this local test run.")
    else:
        print("Observation: Both had nearly identical execution times.")


if __name__ == "__main__":
    main()
