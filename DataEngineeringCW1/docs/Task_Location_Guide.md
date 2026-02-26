# Task Location Guide - TechReads Data Engineering Project

This document maps each task in the assessment brief to the relevant files and locations in your project.

---

## Task 1: Web Scraping

**Location:** `src/scrape_techreads.py`

**Required outputs:**
- Python web scraper using Requests + BeautifulSoup
- CSV output: `data/techreads_books.csv`
- Screenshot evidence of execution

**Relevant files:**
- `src/scrape_techreads.py` - The web scraping script
- `data/techreads_books.csv` - Output CSV file

**Requirements:**
- Extract at least 15 Data Engineering books
- Required fields: Title, Author, Year, Star Rating, Price
- Discussion: 200-250 words with screenshots

---

## Task 2: MySQL Database Pipeline

**Location:** `sql/` directory and `src/import_csv_to_mysql.py`

**Required outputs:**
- Database: `techreads_db`
- Schema diagram: `diagrams/techreads_schema.drawio`
- SQL queries in `sql/` folder
- Screenshot evidence of execution

**Relevant files:**
- `sql/01_create_database.sql` - Create database
- `sql/02_create_table.sql` - Create table schema
- `sql/03_import_csv.sql` - Import CSV data
- `sql/04_task_query.sql` - Select query with sorting
- `src/import_csv_to_mysql.py` - Python script to connect and import
- `diagrams/techreads_schema.drawio` - Schema diagram
- `data/techreads_books.csv` - Source data

**Requirements:**
- Create database `techreads_db`
- Import CSV into MySQL table
- Query 3 columns sorted by price/rating
- Discussion: 200-250 words with screenshots

---

## Task 3: Apache NiFi Dataflow Automation

**Location:** `nifi/DataEngineering_NiFi_Flow_Guide.md` and NiFi configuration

**Required outputs:**
- NiFi dataflow under "DataEngineering" folder
- Exported to local directory (CSV/JSON/Avro)
- Video demonstration with voiceover and camera ON

**Relevant files:**
- `nifi/` directory
- `nifi-2.7.2-bin/nifi-2.7.2/conf/` - NiFi configuration
- `nifi_output/` - Output directory for NiFi flows
- `start_nifi_with_login.bat` / `start_nifi_with_login.ps1` - NiFi startup scripts

**Requirements:**
- Pull data from MySQL database
- Transform if needed
- Save to local directory
- Video demonstration required (single group member)

---

## Task 4: MongoDB Integration & Performance Comparison

**Location:** `src/mongodb_pipeline.py` and `src/benchmark_sql_vs_nosql.py`

**Required outputs:**
- JSON conversion: `src/csv_to_json.py`
- MongoDB database with inserted data
- MongoDB queries
- SQL vs NoSQL performance comparison
- Screenshot evidence

**Relevant files:**
- `src/csv_to_json.py` - Convert CSV to JSON
- `src/mongodb_pipeline.py` - MongoDB integration
- `src/benchmark_sql_vs_nosql.py` - Performance comparison
- `data/techreads_books.json` - JSON output
- `notebook/techreads_pipeline.ipynb` - Jupyter notebook (supporting file)

**Requirements:**
- Convert CSV to JSON
- Insert into MongoDB
- Query by price, year, rating
- Compare SQL vs NoSQL execution time
- Discussion: 200-250 words with screenshots

---

## Report Location

**Template:** `report/TechReads_CW1_Report_Template.md`

**Required sections:**
1. Cover Page (names and IDs of all 4 group members)
2. Table of Contents
3. Task 1: Discussion + Screenshots
4. Task 2: Discussion + Screenshots
5. Task 3: Video Upload
6. Task 4: Discussion + Screenshots
7. Individual Reflection (approx. 750 words)
8. References (IEEE format)

**Supporting file:** `notebook/techreads_pipeline.ipynb` (interactive Python file)

---

## Checklist for Submission

| Requirement | Status | Location |
|------------|--------|----------|
| Task 1: Web Scraper | [ ] | `src/scrape_techreads.py` |
| Task 1: CSV Output | [ ] | `data/techreads_books.csv` |
| Task 2: MySQL DB | [ ] | MySQL `techreads_db` |
| Task 2: Schema Diagram | [ ] | `diagrams/techreads_schema.drawio` |
| Task 2: SQL Queries | [ ] | `sql/` folder |
| Task 3: NiFi Flow | [ ] | NiFi "DataEngineering" folder |
| Task 3: Video | [ ] | Recorded separately |
| Task 4: JSON Data | [ ] | `data/techreads_books.json` |
| Task 4: MongoDB | [ ] | MongoDB database |
| Task 4: Performance Test | [ ] | `src/benchmark_sql_vs_nosql.py` |
| Report PDF | [ ] | `report/` folder |
| Supporting Notebook | [ ] | `notebook/techreads_pipeline.ipynb` |