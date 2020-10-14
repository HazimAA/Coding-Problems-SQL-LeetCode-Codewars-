Difficulty: Hard  
[Link to Question](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/)

----------------------------------------------------------------------------------------

The Employee table holds the salary information in a year.

**Write a SQL to get the cumulative sum of an employee’s salary over a period of 3 months but exclude the most recent month.**


The result should be displayed by ‘Id’ ascending, and then by ‘Month’ descending.

Example
Input

```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
```

Output
```
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
```

**Solution**
```
WITH inner_query as
(
SELECT 
ID,
Month,
SALARY,
ROW_NUMBER() OVER(
PARTITION BY ID
ORDER BY MONTH DESC
) AS ranks
FROM EMPLOYEE
)


SELECT ID, 
MONTH, 
SUM(SALARY) 
OVER(
PARTITION BY ID
ORDER BY MONTH ASC
) AS SALARY
FROM inner_query
WHERE inner_query.ranks != 1
ORDER BY ID, MONTH DESC, SALARY DESC
```


**Alternate Solution:**

```
SELECT
    a.id, 
    a.month,
    SUM(b.salary) Salary
FROM
    Employee a JOIN Employee b ON
    a.id = b.id AND
    a.month - b.month >= 0 AND
    a.month - b.month < 3
GROUP BY
    a.id, a.month
HAVING
    (a.id, a.month) NOT IN (SELECT id, MAX(month) FROM Employee GROUP BY id)
ORDER BY
    a.id, a.month DESC
```
