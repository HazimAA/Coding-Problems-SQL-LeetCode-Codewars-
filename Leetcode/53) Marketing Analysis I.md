Difficulty: Medium  
[Link to Question](https://leetcode.com/problems/market-analysis-i/)
------------------------------------------------------------------------

**Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.**

Users table:
```
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2019-01-01 | Lenovo         |
| 2       | 2019-02-09 | Samsung        |
| 3       | 2019-01-19 | LG             |
| 4       | 2019-05-21 | HP             |
+---------+------------+----------------+
```

Orders table:
```
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2019-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2019-08-04 | 1       | 4        | 2         |
| 5        | 2019-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
```

**SOLUTION:**
```
select u.user_id, u.join_date, c
FROM 
Users u JOIN 
(
SELECT count(item_id) as c, buyer_id
FROM orders
where ORDER_DATE > TO_DATE('2018-12-31','YYYY-MM-DD')
group by buyer_id
) o       
ON u.user_id = o.buyer_id
 ```   
    OR
```
SELECT u.user_id, u.join_date, count(o.order_id) as count
FROM users u JOIN orders o
on u.user_id = o.buyer_id
where o.order_date > TO_DATE('2018-12-31','YYYY-MM-DD')
group by u.user_id, u.join_date
ORDER BY user_id
```
