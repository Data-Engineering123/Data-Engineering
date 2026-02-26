# Coursework Guide: Explanations & Task 3 Video Script

This document provides clear explanations of what is happening in each task of your Data Engineering coursework, helping you write the 1500-word report. It also includes a step-by-step script for your Task 3 Apache NiFi video.

---

## Task 1: Web Scraping

**What is happening:**
We built a Python script (`src/scrape_techreads.py`) to automatically collect book information from the Packt Publishing website, specifically targeting their "Data Engineering" category.

**How it works (for your report):**

1. **Fetching the Page:** The script uses the `requests` library to send an HTTP GET request to the e-commerce webpage. We use a custom "User-Agent" header to ensure the website doesn't block our request, making us look like a standard web browser.
2. **Parsing HTML:** Once the HTML is fetched, we pass it to `BeautifulSoup`. The script searches for specific product cards using CSS selectors (e.g., `[data-carousel-item]`).
3. **Extracting Data Fields:** Packt uses custom `data-analytics-item-*` HTML attributes to store product information. The script extracts the *Title*, *Author*, *Publication Year*, *Price*, and *Star Rating* from these specific attributes. Defensive programming techniques (like `try/except` blocks) ensure that if a field like price or year is missing, the script won't crash.
4. **Structuring & Saving:** We collect these details into a list of Python dictionaries. The `pandas` library is then used to convert this list into a structured DataFrame. Finally, `pandas` exports this data into a CSV file (`data/techreads_books.csv`). We also enforce a check to ensure at least 15 books are recorded.

---

## Task 2: MySQL Database Pipeline

**What is happening:**
We transition the extracted, flat CSV data into a structured relational database using MySQL.

**How it works (for your report):**

1. **Schema Creation:** We designed a robust relational schema (implemented in `sql/02_create_table.sql`). The table `techreads_books` uses appropriate data types: `VARCHAR` for strings (Title, Author), `DECIMAL` for the Price and Rating, and `INT` for the Publication Year. A vital part of this schema is setting an `id` as the Primary Key for absolute data integrity.
2. **Data Importation:** The CSV is loaded into the `techreads_db` database using standard SQL `LOAD DATA INFILE` commands (or via Python's pandas-to-SQL functionality/import scripts).
3. **Querying:** To demonstrate data retrieval, we execute a query (`sql/04_task_query.sql`) that extracts three specific columns: `title`, `price_gbp`, and `rating`. We use the `ORDER BY` clause to sort the results logically—first by `rating` in descending order (highest rated first), and then by `price` ascending (cheaper books first).

**For your report:** Include the schema diagram (draw.io) and justify why `DECIMAL` is better than `FLOAT` for financial values (prices) to avoid rounding errors.

---

## Task 4: MongoDB Integration & Performance Comparison

**What is happening:**
We explore NoSQL databases as an alternative to structured SQL, inserting our data into MongoDB and comparing query execution times.

**How it works (for your report):**

1. **Data Conversion & Insertion:** First, the scraped CSV is converted to JSON format (`src/csv_to_json.py`). Using the `pymongo` Python library, we connect to a local MongoDB instance and insert this JSON document collection into the `techreads_mongo_db` database, inside the `books` collection.
2. **MongoDB Querying:** We perform a filter query (`src/mongodb_pipeline.py`) using MongoDB's JSON-like query syntax, specifically looking for books with a high rating (`$gte: 4`) and an affordable price (`$lt: 40`).
3. **Benchmarking (SQL vs. NoSQL):** The script `src/benchmark_sql_vs_nosql.py` executes equivalent queries against both MySQL and MongoDB sequentially. It uses Python's `time.perf_counter()` to precisely measure how many milliseconds each database takes to return the results.
4. **Discussion Points:** In your report, mention that MySQL is highly structured (ACID compliant) and great for relational joins, whereas MongoDB (NoSQL) offers aggregate flexibility and schema-less design, which is excellent for semi-structured e-commerce catalogs. Discuss the benchmark results: often, for flat, single-table reads without joins, NoSQL can be extremely fast, but SQL indexing can level the playing field.

---

## Task 3: Apache NiFi Video Script

**Requirements:** Max a few minutes, upload video, voiceover required, Camera ON showing your face.

**Preparation:**

- Have NiFi running and open in your browser (`http://localhost:8080/nifi`).
- Ensure MySQL is running and the database is populated.
- Have the camera recording your face and your screen.

**Script:**

*(Start Recording - Look at the camera)*
**You:** "Hello, my name is [Your Name] and my student ID is [Your ID]. Today I will be demonstrating Task 3 of the Data Engineering Coursework, showing an automated Apache NiFi dataflow."

*(Share screen showing the NiFi Canvas)*
**You:** "As you can see, I am in the Apache NiFi user interface. I have created a Process Group named 'DataEngineering' as required by the brief. Let's enter the group."

*(Double-click into the DataEngineering process group showing the processors)*
**You:** "Here is our automated ingestion pipeline. The goal is to automatically extract book data from our MySQL database, transform it into JSON format, and save it to a local directory."

*(Click on the first processor: `QueryDatabaseTable` or `ExecuteSQL`)*
**You:** "Our pipeline starts with the `QueryDatabaseTable` (or `ExecuteSQL`) processor. I've configured this with a JDBC Connection Pool pointing to our local MySQL `techreads_db`. This processor securely connects to the database and pulls the records from the `techreads_books` table."

*(Hover over the connection line to the next processor)*
**You:** "The data is extracted in Avro format. It then flows into the `ConvertRecord` processor."

*(Click on the `ConvertRecord` processor)*
**You:** "In the `ConvertRecord` processor, I have configured an Avro Reader and a JSON Record Set Writer. This transforms our structured database rows into a flexible JSON format, bridging the gap between our relational and NoSQL ecosystems."

*(Click on the `PutFile` processor)*
**You:** "Finally, the JSON data moves to the `PutFile` processor. I have configured the directory property to point to our local output folder. This automatically saves the pipeline's output locally without manual intervention."

*(Start the processors by right-clicking and hitting 'Start' on all of them)*
**You:** "I will now start the processors to demonstrate the flow. We can see the data queuing and passing through the system successfully."

*(Open the output folder in Windows File Explorer)*
**You:** "And if I open my local output directory, you can see the generated JSON file has automatically appeared, completing the automated data delivery pipeline."

*(Look back at camera)*
**You:** "This demonstrates how manual script executions are replaced by scalable automation. Thank you for watching." *(Stop Recording)*

---

## Other Coursework Requirements to Remember

1. **Individual Reflection (750 words):** You MUST write this yourself without AI. Discuss exactly what *you* did (e.g., "I focused on setting up the MySQL schemas" or "I wrote the BeautifulSoup logic"), what you learned about pipelines, and challenges you faced (e.g., handling missing HTML tags on PacktPub, or getting NiFi database connections to work).
2. **References:** Use IEEE format. Reference any libraries (Pandas, BeautifulSoup), tools (Apache NiFi, MongoDB), or websites (StackOverflow, MySQL Docs) that you consulted.
3. **Formatting:** 12-point Times New Roman font, double-spaced, 1-inch margins.
4. **Jupyter Notebook:** Ensure you submit an interactive `.ipynb` file as your supporting code artifact alongside the PDF report. The repository currently has `notebook/techreads_pipeline.ipynb` which you can use for this.
