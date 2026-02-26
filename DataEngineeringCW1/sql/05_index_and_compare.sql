<<<<<<< HEAD
-- Task 4 support: measure query performance with and without index.
-- NOTE: MariaDB/phpMyAdmin may not support `EXPLAIN ANALYZE`.
-- Use `EXPLAIN` (or `EXPLAIN FORMAT=JSON`) for compatibility.
USE techreads_db;

-- Query to benchmark
EXPLAIN
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;

-- Add index to improve filtering/sorting
CREATE INDEX idx_rating_price ON techreads_books (rating, price_gbp);

EXPLAIN
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;
=======
-- Task 4 support: measure query performance with and without index.
-- NOTE: MariaDB/phpMyAdmin may not support `EXPLAIN ANALYZE`.
-- Use `EXPLAIN` (or `EXPLAIN FORMAT=JSON`) for compatibility.
USE techreads_db;

-- Query to benchmark
EXPLAIN
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;

-- Add index to improve filtering/sorting
CREATE INDEX idx_rating_price ON techreads_books (rating, price_gbp);

EXPLAIN
SELECT title, price_gbp, rating
FROM techreads_books
WHERE rating >= 4 AND price_gbp < 40
ORDER BY rating DESC, price_gbp ASC;
>>>>>>> 2a194767c6d33f5956eb227f2088e57a9185b9ab
