# TechReads CW1 – AI-Assisted Submission Pack

This package gives you everything that can be prepared in advance for the assessment, except the human-only parts (demo delivery, camera/voice recording, and personal reflection from your own lived contribution).

## What is included

1. **Web scraping pipeline (Task 1)**
   - `src/scrape_techreads.py`
   - Produces: `data/techreads_books.csv`
2. **MySQL pipeline assets (Task 2)**
   - `sql/01_create_database.sql`
   - `sql/02_create_table.sql`
   - `sql/03_import_csv.sql`
   - `sql/04_task_query.sql`
   - `sql/05_index_and_compare.sql`
3. **MongoDB integration assets (Task 4)**
   - `src/csv_to_json.py`
   - `src/mongodb_pipeline.py`
   - `src/benchmark_sql_vs_nosql.py`
4. **NiFi implementation guide (Task 3)**
   - `nifi/DataEngineering_NiFi_Flow_Guide.md`
5. **Report and evidence support**
   - `report/TechReads_CW1_Report_Template.md`
   - `docs/Screenshots_And_Evidence_Checklist.md`
   - `diagrams/techreads_schema.drawio`
6. **Notebook supporting file**
   - `notebook/techreads_pipeline.ipynb`

---

## Quick-start order

1. Install dependencies:

```bash
pip install requests beautifulsoup4 pandas pymysql mysql-connector-python pymongo
```

2. Run Task 1 scraper:

```bash
python src/scrape_techreads.py
```

3. Set up MySQL and run SQL scripts in order (`01` → `05`).

4. Convert CSV to JSON and push to MongoDB:

```bash
python src/csv_to_json.py
python src/mongodb_pipeline.py
```

5. Run SQL vs NoSQL benchmark:

```bash
python src/benchmark_sql_vs_nosql.py
```

6. Build NiFi flow using `nifi/DataEngineering_NiFi_Flow_Guide.md`, record demo video (voice + camera ON).

7. Paste your screenshots and actual outputs into the report template and export to PDF.

---

## Important notes

- The scraper uses `books.toscrape.com` (a common educational e-commerce scraping target).
- Task field requirement is satisfied with at least 5 fields: `title`, `price_gbp`, `rating`, `availability`, `product_url`.
- If your tutor strictly requires `author` and `publication_year`, switch target website and extend parser accordingly.
- Keep your IEEE references genuine and verifiable.
