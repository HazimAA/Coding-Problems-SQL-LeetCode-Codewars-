Difficulty: Easy

[Link to Question]()

---------------------------------


**Select all employee's name and bonus whose bonus is < 1000.**

Table: Employee
```
+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId is the primary key column for this table.
```
Table: Bonus
```
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId is the primary key column for this table.
```
Example ouput:
```
+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+
```

**SOLUTION:**
```
SELECT e.NAME, b.BONUS 
FROM EMPLOYEE e LEFT OUTER JOIN BONUS b
ON e.EMPID = b.EMPID
WHERE b.BONUS < 1000 OR b.BONUS is null
;
```
