# TechReads Retail Analytics – Data Engineering CW1 Report

> **Formatting reminder**: Times New Roman, 12pt, double-spaced, 1-inch margins, IEEE references.

---

## Cover Page

- Module: Data Engineering (CMP-X304-0)
- Assessment: Coursework 1
- Group members (Name + Student ID):
  - Member 1:
  - Member 2:
  - Member 3:
  - Member 4:
- Submission date:

---

## Table of Contents

*(Auto-generate in Word before final PDF export.)*

---

## Task 1: Web Scraping (200–250 words)

### Implementation summary
The scraping component was developed in Python using `requests`, `BeautifulSoup`, and `pandas`. The target source is the Packt Publishing data engineering catalogue at `https://www.packtpub.com/en-gb/data/concept/data-engineering`. The scraper downloads the listing page, selects all `div.product-card-content` elements, and extracts seven fields per record: `title`, `author`, `publication_year`, `price_gbp`, `rating`, `availability`, and `product_url`.

Because author names are not present in the listing cards, the scraper visits each individual product page to retrieve them from the `div.authors` element, applying a 0.5-second polite delay between requests. Publication year is parsed from the date metadata (e.g., "Mar 2024" → 2024), and rating is stored as a decimal (e.g., 4.7) to preserve Packt's fractional star scale. Data validation confirms at least 15 records before writing to `techreads_books.csv`.

### Rationale
`requests` was selected for lightweight HTTP retrieval, BeautifulSoup for robust DOM parsing, and pandas for reliable data shaping/export. This combination provides a practical ETL-style extraction layer well-suited to structured product catalogues like Packt's data engineering section.

### Evidence placeholders
- Figure 1: Script execution output
- Figure 2: CSV preview

---

## Task 2: MySQL Database Pipeline (200–250 words)

### Implementation summary
MySQL was configured locally to host structured catalogue data in `techreads_db`. A table named `techreads_books` was created with typed attributes (`DECIMAL` for price, `TINYINT` for rating, and `VARCHAR` for textual fields). The scraped CSV was imported using `LOAD DATA LOCAL INFILE`, enabling efficient bulk ingestion.

To satisfy analytical requirements, an SQL query selected three columns (`title`, `price_gbp`, `rating`) and sorted results by rating and price. This demonstrates retrieval for dashboard-style use and ranking analysis. A schema diagram was produced in draw.io to visualise table structure and support documentation clarity.

### Rationale
MySQL was chosen for consistency, mature SQL support, and straightforward integration with NiFi ingestion processors. Relational storage is appropriate for well-defined, tabular product records and repeatable reporting queries.

### Evidence placeholders
- Figure 3: Database/table creation
- Figure 4: CSV import
- Figure 5: Sorted SQL query output
- Figure 6: Schema diagram

---

## Task 3: Apache NiFi Dataflow Automation

### Implementation summary
An Apache NiFi process group named `DataEngineering` was created to automate MySQL-to-file ingestion. The flow uses database processors to fetch records from `techreads_books`, applies optional record transformation, and writes structured output to a local directory in JSON (or CSV) format.

### Rationale
NiFi introduces no-code/low-code orchestration, scheduling, provenance, and operational visibility. This reduces manual execution dependency and supports scalable ingestion workflows in production-style environments.

### Evidence placeholders
- Video: NiFi flow build and execution (voiceover + camera ON)

---

## Task 4: MongoDB Integration & SQL vs NoSQL Comparison (200–250 words)

### Implementation summary
The dataset was converted from CSV to JSON and loaded into MongoDB (`techreads_mongo_db.books`). Filter queries were executed using conditions on price and rating to mirror SQL logic as closely as possible. Query duration for both systems was measured with Python timing methods.

In SQL, structured filtering and sorting are expressed declaratively and benefit strongly from composite indexing (e.g., `(rating, price_gbp)`). In MongoDB, flexible document storage allows easier schema evolution and semi-structured extensions, while query speed depends on index strategy and dataset characteristics.

### Comparison
For this task’s small local dataset, execution times are expected to be close, with differences often dominated by local environment overhead. SQL is generally advantageous for strict relational analytics and joins, while MongoDB is advantageous where schema flexibility and rapid iteration are priorities. Therefore, a hybrid architecture (MySQL for structured dashboards + MongoDB for exploratory/semi-structured analytics) best fits the TechReads scenario.

### Evidence placeholders
- Figure 7: JSON conversion output
- Figure 8: Mongo insert + query output
- Figure 9: SQL vs Mongo timing output

---

## Individual Reflection (~750 words, authentic and personal)

> Write this in your own words.

Recommended structure:
1. Your specific contribution across Tasks 1–4
2. What you learned technically (tools, debugging, data modelling, automation)
3. Challenges faced (data quality, setup issues, coordination) and how resolved
4. Team collaboration and role management
5. What you would improve in the next iteration

---

## References (IEEE style)

[1] Python Software Foundation, “Python 3 Documentation.” [Online]. Available: https://docs.python.org/3/

[2] Beautiful Soup Documentation, “Beautiful Soup 4 Documentation.” [Online]. Available: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

[3] MySQL, “MySQL 8.0 Reference Manual.” [Online]. Available: https://dev.mysql.com/doc/

[4] Apache NiFi, “NiFi Documentation.” [Online]. Available: https://nifi.apache.org/documentation/

[5] MongoDB, “MongoDB Manual.” [Online]. Available: https://www.mongodb.com/docs/

*(Add any additional sources you actually used.)*
