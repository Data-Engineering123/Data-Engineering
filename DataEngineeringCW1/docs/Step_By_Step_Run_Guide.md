# Step-by-Step Run Guide (with comments)

This file explains exactly how to run every part of the coursework code in order.

> Run all commands from this folder:
>
> `c:\Users\alvi9\MyWork\Data Engineering - Copy`

---

## 0) Open terminal in project folder

```powershell
# Opens PowerShell in the current project folder (if not already there)
cd "c:\Users\alvi9\MyWork\Data Engineering - Copy"
```

---

## 1) Install Python dependencies

```powershell
# Install required Python libraries used by scraper, CSV/JSON processing, MySQL and MongoDB scripts
python -m pip install requests beautifulsoup4 pandas pymysql mysql-connector-python pymongo
```

If you see `ModuleNotFoundError: No module named 'pandas'`, this step is required and fixes it.

---

## 2) Run Task 1 scraper (create CSV)

```powershell
# Runs web scraping script and saves output file to data/techreads_books.csv
python src/scrape_techreads.py
```

Expected result:
- Terminal prints: `Saved 15 records to data\techreads_books.csv`
- File created: `data/techreads_books.csv`

---

## 3) Create MySQL database + table

### Option A: MySQL Command Line

```powershell
# Open MySQL shell
mysql -u root -p
```

Then run:

```sql
-- Create database
SOURCE sql/01_create_database.sql;

-- Create table
SOURCE sql/02_create_table.sql;
```

### Option B: MySQL Workbench

1. Open each SQL file (`01` then `02`) in Workbench.
2. Execute each script.

### Option C: phpMyAdmin (important difference)

In phpMyAdmin, **do not use `SOURCE ...`** commands. `SOURCE` works in MySQL CLI, not phpMyAdmin SQL box.

Do this instead:

1. Open file `sql/01_create_database.sql` in VS Code.
2. Copy only the SQL content:

```sql
CREATE DATABASE IF NOT EXISTS techreads_db;
USE techreads_db;
```

3. Paste into phpMyAdmin **SQL** tab and click **Go**.
4. Open file `sql/02_create_table.sql`, copy its SQL content, paste into phpMyAdmin SQL tab, and click **Go**.

If your server is MariaDB/phpMyAdmin, this method is the correct one.

---

## 4) Import CSV into MySQL

Before import:
- Ensure `sql/03_import_csv.sql` path is correct.
- Ensure MySQL allows local infile. If needed run:

```sql
SET GLOBAL local_infile = 1;
```

Now import:

```sql
SOURCE sql/03_import_csv.sql;
```

If you get this error:

`#2068 - LOAD DATA LOCAL INFILE is forbidden`

use one of the fallback methods below.

### phpMyAdmin way for Step 4 (recommended if using phpMyAdmin)

1. In phpMyAdmin left panel, click database `techreads_db`.
2. Click table `techreads_books`.
3. Open **Import** tab.
4. Choose file: `data/techreads_books.csv`.
5. Format: **CSV**.
6. Tick option indicating first row has column names (if available in your version).
7. Click **Go**.

### Python fallback (works even when LOCAL INFILE is blocked)

1. Open `src/import_csv_to_mysql.py`.
2. Set your MySQL username/password in `MYSQL_CONFIG`.
3. Run:

```powershell
# Inserts CSV rows into techreads_books using mysql-connector (no LOCAL INFILE needed)
python src/import_csv_to_mysql.py
```

Expected result:
- Terminal prints inserted row count.

---

## 5) Run required Task 2 SQL query

```sql
-- Returns 3 selected columns sorted by rating and price
SOURCE sql/04_task_query.sql;
```

### phpMyAdmin way for Step 5

If using phpMyAdmin, do **not** use `SOURCE`.

1. Select database `techreads_db` in left panel.
2. Open **SQL** tab.
3. Paste and run this query:

```sql
SELECT
    title,
    price_gbp,
    rating
FROM techreads_books
ORDER BY rating DESC, price_gbp ASC;
```

4. Take screenshot of the query result for your report.

Take screenshot of the result table for report evidence.

---

## 6) Run SQL index/performance query (Task 4 support)

```sql
-- Shows EXPLAIN before and after index creation
SOURCE sql/05_index_and_compare.sql;
```

### phpMyAdmin way for Step 6 (still MySQL)

Yes — this is still your **MySQL Task 6**, just executed in phpMyAdmin’s SQL tab.

Use one of these based on your server engine/version:

#### Option A: MySQL 8+ (preferred when supported)

```sql
EXPLAIN ANALYZE
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;
```

Then create the index:

```sql
CREATE INDEX idx_rating_price ON techreads_books (rating, price_gbp);
```

Then run the same `EXPLAIN ANALYZE` query again.

#### Option B: MariaDB / older MySQL fallback

If phpMyAdmin throws syntax error on `EXPLAIN ANALYZE`, use:

```sql
EXPLAIN
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;
```

Then create the index:

```sql
CREATE INDEX idx_rating_price ON techreads_books (rating, price_gbp);
```

Then run EXPLAIN again:

```sql
EXPLAIN
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;
```

If you get "Duplicate key name 'idx_rating_price'", the index already exists, so skip index creation and just run the second EXPLAIN.

Take screenshots of both plans/timings.

---

## 7) Convert CSV to JSON (for MongoDB)

```powershell
# Converts data/techreads_books.csv to data/techreads_books.json
python src/csv_to_json.py
```

Expected result:
- File created: `data/techreads_books.json`

---

## 8) Insert into MongoDB and run Mongo query

Make sure MongoDB server is running locally first.

### Quick check: is MongoDB installed?

Run in PowerShell:

```powershell
mongod --version
```

- If version appears: MongoDB is installed.
- If command not found: install **MongoDB Community Server** (and MongoDB Shell) first.

### If `'mongod' is not recognized` (your current case)

Install MongoDB Community Server, then reopen PowerShell.

#### Option A: Install with winget (fastest)

```powershell
winget install --id MongoDB.Server --source winget
winget install --id MongoDB.Shell --source winget
```

After install, close and reopen terminal, then test:

```powershell
mongod --version
```

#### Option B: Manual installer

1. Download Community Server from MongoDB official site.
2. During setup, keep **Install MongoDB as a Service** checked.
3. Finish installation and reopen terminal.

Install links:
- MongoDB Community Server: https://www.mongodb.com/try/download/community
- MongoDB Shell (mongosh): https://www.mongodb.com/try/download/shell

### Start MongoDB on Windows (try in this order)

```powershell
# If MongoDB is installed as a Windows service
net start MongoDB
```

If that says service not found, start mongod manually:

```powershell
# Create data directory once (if missing)
mkdir C:\data\db

# Start MongoDB server in this terminal window
mongod --dbpath C:\data\db
```

Keep the `mongod` window open, then use a new terminal for the next command.

If `mongod` command is not recognized after installation, use full path (example):

```powershell
"C:\Program Files\MongoDB\Server\8.0\bin\mongod.exe" --dbpath C:\data\db
```

You can also add this folder to PATH permanently:

`C:\Program Files\MongoDB\Server\8.0\bin`

```powershell
# Loads JSON into techreads_mongo_db.books and runs filter query
python src/mongodb_pipeline.py
```

Expected result:
- Prints inserted document count
- Prints query time and sample results
- Prints indexed query time

If you see "connection refused on localhost:27017", MongoDB is not running yet.

---

## 9) Run SQL vs NoSQL benchmark script

Before running:
- If you get `1045 Access denied for user 'root'@'localhost'`, set correct MySQL credentials first.

### Option A: Set credentials for current PowerShell session

```powershell
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="YOUR_REAL_PASSWORD"
$env:MYSQL_DATABASE="techreads_db"
```

### Option B: Edit script defaults directly

Edit `src/benchmark_sql_vs_nosql.py` and set `MYSQL_CONFIG` values for your local MySQL account.

```powershell
# Compares similar query time in MySQL and MongoDB
python src/benchmark_sql_vs_nosql.py
```

Take screenshot of output for Task 4 comparison section.

---

## 10) Run NiFi flow (Task 3)

Use this file for exact processor setup:

- `nifi/DataEngineering_NiFi_Flow_Guide.md`

What to do:
1. Build process group named **DataEngineering**.
2. Configure DB connection and processors.
3. Run flow and verify output files.
4. Record demo video (voice + camera ON).

---

## 11) Complete report and submission files

Use template:

- `report/TechReads_CW1_Report_Template.md`

Add:
- Your real screenshots
- Your measured timings
- Your authentic individual reflection (~750 words)
- Your group details on cover page

Then export to PDF and submit with:
- PDF report
- `notebook/techreads_pipeline.ipynb`

---

## Quick troubleshooting

### Error: `No module named pandas`

```powershell
python -m pip install pandas
```

### Error connecting to MySQL

- Check service is running
- Check username/password in script
- Ensure database/table were created

### Error connecting to MongoDB

- Start MongoDB service
- Confirm URI: `mongodb://localhost:27017/`

### CSV import fails in MySQL

- Verify full file path in `sql/03_import_csv.sql`
- Enable `local_infile`
