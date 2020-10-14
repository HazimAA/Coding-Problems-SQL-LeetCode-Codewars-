**Write a SQL query to find all duplicate emails in a table named Person.**

Difficulty: Easy
[Link to Question](https://leetcode.com/problems/duplicate-emails/)

```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```

For example, your query should return the following for the above table:

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

**Solution:**

```
SELECT Email FROM
(
    SELECT Email, COUNT(Email) as num
FROM Person 
GROUP BY Email 
)
WHERE num > 1
;
```
