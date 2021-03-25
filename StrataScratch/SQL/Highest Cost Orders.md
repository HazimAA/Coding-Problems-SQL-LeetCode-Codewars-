Difficulty: Hard  
[Link to Question](https://platform.stratascratch.com/coding-question?id=9915&python=)  
------------------------------------------------------

Highest Cost Orders
Find the customer with the highest total order cost between 2019-02-01 to 2019-05-01. Output their first name, total cost of their items, and the date.
For simplicity, you can assume that every first name in the dataset is unique.

(The Question wants us to find the Highest Daily Order cost and the Customers who have spent an amount equivalent to it on a single day.)

**Solution:**
```
SELECT t.* FROM 
(
    SELECT 
    DISTINCT c.first_name,
    o.order_date,
    SUM(o.order_cost*o.order_quantity) OVER (PARTITION BY o.cust_id, o.order_date) as order_cost_new 
    FROM orders o JOIN customers c ON o.cust_id = c.id
    WHERE o.order_date BETWEEN '2019-02-01' AND '2019-05-01'
    ORDER BY order_cost_new DESC, order_date
) t
WHERE t.order_cost_new = 
(
    SELECT 
    SUM(o.order_cost*o.order_quantity) OVER (PARTITION BY o.cust_id, o.order_date) as total_daily_order_cost_filtered 
    FROM orders o JOIN customers c ON o.cust_id = c.id
    WHERE o.order_date BETWEEN '2019-02-01' AND '2019-05-01'
    ORDER BY total_daily_order_cost_filtered DESC, order_date
    LIMIT 1
)
;
```

OR

```
SELECT first_name,
       order_date,
       sum(total_order_cost)
FROM
  (SELECT first_name,
          order_cost * order_quantity AS total_order_cost,
          order_date
   FROM orders o
   LEFT JOIN customers c ON o.cust_id = c.id
   WHERE order_date BETWEEN '2019-02-1' AND '2019-05-1' ) a
GROUP BY first_name,
         order_date
HAVING sum(total_order_cost) =
  (SELECT max(total_order_cost)
   FROM
     (SELECT sum(order_cost * order_quantity) AS total_order_cost
      FROM orders
      WHERE order_date BETWEEN '2019-02-1' AND '2019-05-1'
      GROUP BY cust_id,
               order_date) b )
```
