-- after "FROM purchases" add code to rows with a date of "2018-11-01" or earlier in the "purchased_at" column

SELECT *
FROM purchases
WHERE purchased_at <= "2018-11-01";


-- after "FROM purchases" add code to get rows where the "name" contains "pudding"

SELECT *
FROM purchases
WHERE name LIKE "%pudding%";

/*
after "FROM purchases" use the NOT operator to get rows where
the "character_name" column is not "Ken the Ninja"
*/

SELECT *
FROM purchases
WHERE NOT character_name = "Ken the Ninja";

-- after "FROM purchases" add code to get rows
-- where the "price" column is NULL

SELECT *
FROM purchases
WHERE price IS NULL;

-- after "FROM purchases" add code to get rows where the "category" column is "food"
-- and the "character_name" column is "Master Wooly"

SELECT *
FROM purchases
WHERE category = "food"
AND character_name = "Master Wooly";

-- after "FROM purchases" add code to get a maximum of 5 rows
-- in descending order by the "price" column

SELECT *
FROM purchases
ORDER BY price DESC
LIMIT 5;
