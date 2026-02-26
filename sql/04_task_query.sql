-- Task 2 mandatory query:
-- Extract three columns and sort by one column.

USE techreads_db;

SELECT
    title,
    price_gbp,
    rating
FROM techreads_books
ORDER BY rating DESC, price_gbp ASC;
