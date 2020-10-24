Difficulty: 6 Kyu  
[Link to Question](https://www.codewars.com/kata/5982020284a83baf2f00001c/sql)  
[Reference](https://tapoueh.org/blog/2013/07/simple-case-for-pivoting-in-sql/)
------------------------------------------------

**You need to build a pivot table WITHOUT using CROSSTAB function. Having two tables products and details you need to select a pivot table of products with counts of details occurrences (possible details values are ['good', 'ok', 'bad'].**

Results should be ordered by product's name.

Model schema for the kata is:

![ER Pic](https://i.imgur.com/81Ww3YH.png)

your query should return table with next columns

    name
    good
    ok
    bad

Compare your table to the expected table to view the expected results.

**Solution**
```
SELECT p.name,
  COUNT(p.name) filter (where d.detail ='good') as good,
  COUNT(p.name) filter (where d.detail ='ok') as ok,
  COUNT(p.name) filter (where d.detail ='bad') as bad
FROM products p JOIN details d
ON p.id = d.product_id
GROUP BY p.name
ORDER by p.name
```
