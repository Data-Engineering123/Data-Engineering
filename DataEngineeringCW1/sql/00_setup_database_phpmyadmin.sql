-- ============================================
-- TechReads Database Setup for phpMyAdmin
-- ============================================
-- Instructions for phpMyAdmin:
-- 1. Open phpMyAdmin (http://localhost/phpmyadmin)
-- 2. Click on "SQL" tab at the top
-- 3. Copy and paste the entire script below
-- 4. Click "Go" to execute

-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS techreads_db;
USE techreads_db;

-- Step 2: Drop table if exists (optional, for clean install)
DROP TABLE IF EXISTS techreads_books;

-- Step 3: Create the books table
CREATE TABLE IF NOT EXISTS techreads_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NULL,
    publication_year INT NULL,
    price_gbp DECIMAL(10,2) NOT NULL,
    rating TINYINT NOT NULL,
    availability VARCHAR(120) NULL,
    product_url VARCHAR(500) NULL,
    scraped_at_utc VARCHAR(60) NULL
);

-- Step 4: Insert sample data (15 Data Engineering books from PacktPub)
-- These are Data Engineering related books
INSERT INTO techreads_books (title, author, publication_year, price_gbp, rating, availability, product_url, scraped_at_utc) VALUES
('Solutions Architect''s Handbook', 'Packt Publishing', 2024, 44.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/solutions-architects-handbook-9781835084366', NOW()),
('Data Engineering with Databricks Cookbook', 'Packt Publishing', 2024, 37.99, 4, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-engineering-with-databricks-cookbook-9781837632060', NOW()),
('Data Engineering with dbt', 'Packt Publishing', 2023, 37.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-engineering-with-dbt-9781803241883', NOW()),
('Getting Started with DuckDB', 'Packt Publishing', 2024, 41.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/getting-started-with-duckdb-9781803232539', NOW()),
('Data Engineering with Google Cloud Platform', 'Packt Publishing', 2024, 31.99, 4, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-engineering-with-google-cloud-platform-9781835085363', NOW()),
('Databricks Certified Associate Developer for Apache Spark Using Python', 'Packt Publishing', 2024, 26.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/databricks-certified-associate-developer-for-apache-spark-using-python-9781804616208', NOW()),
('Mastering Azure Databricks for Data Engineers', 'Packt Publishing', 2024, 90.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/mastering-azure-databricks-for-data-engineers-9781836200437', NOW()),
('Data Engineering with Python', 'Packt Publishing', 2020, 38.99, 3, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-engineering-with-python-9781839212307', NOW()),
('Apache Spark 3 for Data Engineering and Analytics with Python', 'Packt Publishing', 2021, 45.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/apache-spark-3-for-data-engineering-and-analytics-with-python-9781803244303', NOW()),
('Data Quality in the Age of AI', 'Packt Publishing', 2024, 56.99, 3, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-quality-in-the-age-of-ai-9781835088562', NOW()),
('Big Data on Kubernetes', 'Packt Publishing', 2024, 29.99, 0, 'In Stock', 'https://www.packtpub.com/en-gb/product/big-data-on-kubernetes-9781835468999', NOW()),
('The Ultimate Guide to Snowpark', 'Packt Publishing', 2024, 31.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/the-ultimate-guide-to-snowpark-9781805124450', NOW()),
('Azure Data Engineer Associate Certification Guide', 'Packt Publishing', 2024, 37.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/azure-data-engineer-associate-certification-guide-9781805127918', NOW()),
('Data Engineering with AWS', 'Packt Publishing', 2021, 48.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-engineering-with-aws-9781800569041', NOW()),
('Data Modeling with Snowflake', 'Packt Publishing', 2023, 48.99, 5, 'In Stock', 'https://www.packtpub.com/en-gb/product/data-modeling-with-snowflake-9781837632787', NOW());

-- Step 5: Verify data was inserted
SELECT COUNT(*) AS total_books FROM techreads_books;

-- Step 6: Sample query - Extract three columns sorted by rating
SELECT
    title,
    price_gbp,
    rating
FROM techreads_books
ORDER BY rating DESC, price_gbp ASC;

-- ============================================
-- End of Setup Script
-- ============================================