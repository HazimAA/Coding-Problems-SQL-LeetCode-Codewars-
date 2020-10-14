Difficulty: 5 Kyu

[Link to Question](https://www.codewars.com/kata/58126aa90ea99769e7000119)

----------------------------------------------------------------------------

**For this challenge you need to PIVOT data. You have two tables, products and details. Your task is to pivot the rows in products to produce a table of products 
which have rows of their detail. Group and Order by the name of the Product.**

Tables and relationship below:

![ER Pic](https://i.imgur.com/81Ww3YH.png)

You must use the CROSSTAB statement to create a table that has the schema as below:
CROSSTAB table.
``
    name
    good
    ok
    bad
``
Compare your table to the expected table to view the expected results. 

**Solution:**
```
SELECT * 
FROM crosstab(
'SELECT p.name, d.detail, COUNT(d.id) 
FROM products p JOIN details d
ON p.id = d.product_id
GROUP BY p.name, d.detail
ORDER BY 1,2'
)
AS 
result (name TEXT, bad bigint, good bigint, ok bigint);
```
