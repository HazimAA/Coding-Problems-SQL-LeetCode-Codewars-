Difficulty: Medium  
[Link to Question](https://platform.stratascratch.com/coding-question?id=10142&python=)
-------------------------------------------------------------------------

Find customers who didn't place orders from 2019-02-01 to 2019-03-01. Output customer's first name.

**Solution:**
```
SELECT first_name
FROM customers 
WHERE id NOT IN
(
    SELECT cust_id
    FROM orders
    WHERE order_date BETWEEN '2019-02-01' AND '2019-03-01'
)
;
```
