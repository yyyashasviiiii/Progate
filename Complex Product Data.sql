
-- get the specified data for men's, women's, and gender neutral products
SELECT items.gender, SUM(price) AS "sales total"
FROM items
JOIN sales_records
ON items.id = sales_records.item_id
GROUP BY items.gender;


-- get the specified data for the top 5 products with the highest sales
SELECT items.id, items.name, SUM(price) AS "sales total"
FROM items
JOIN sales_records
ON items.id = sales_records.item_id
GROUP BY items.id
ORDER BY SUM(price) DESC
LIMIT 5;


SELECT items.id, items.name, items.price * COUNT(*) AS "sales total"            
FROM sales_records            
JOIN items            
ON sales_records.item_id = items.id            
GROUP BY items.id, items.name, items.price            
HAVING (COUNT(*) * items.price) > (            
  SELECT COUNT(*) * items.price            
  FROM sales_records            
  JOIN items            
  ON sales_records.item_id = items.id            
  WHERE items.name = "grey hoodie"            
  );
  
  
