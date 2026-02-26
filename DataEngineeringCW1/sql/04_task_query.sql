<<<<<<< HEAD
-- Task 2 mandatory query:
-- Extract three columns and sort by one column.

USE techreads_db;

SELECT
    title,
    price_gbp,
    rating
FROM techreads_books
ORDER BY rating DESC, price_gbp ASC;
=======
-- Task 2 mandatory query:
-- Extract three columns and sort by one column.

USE techreads_db;

SELECT
    title,
    price_gbp,
    rating
FROM techreads_books
ORDER BY rating DESC, price_gbp ASC;
>>>>>>> 2a194767c6d33f5956eb227f2088e57a9185b9ab
