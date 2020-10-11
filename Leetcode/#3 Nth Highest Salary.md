**Write a SQL query to get the nth highest salary from the Employee table.**

Difficulty: Medium

[Link to Question](https://leetcode.com/problems/nth-highest-salary/)

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.


**Solution**

```
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */   
 

SELECT max(Salary) INTO result 
FROM (
SELECT Salary, dense_rank() OVER(ORDER BY Salary DESC) as dense_rank
FROM Employee
) 
WHERE dense_rank = N;

  RETURN result;
END;
```
