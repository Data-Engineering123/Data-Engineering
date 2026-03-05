-- Task 2: Import CSV into MySQL

USE techreads_db;

LOAD DATA LOCAL INFILE 'data/techreads_books.csv'
INTO TABLE techreads_books
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(title, author, publication_year, price_gbp, rating, availability, product_url, scraped_at_utc);
