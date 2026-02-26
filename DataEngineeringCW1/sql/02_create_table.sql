-- Task 2: Create table for scraped book data
USE techreads_db;

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
