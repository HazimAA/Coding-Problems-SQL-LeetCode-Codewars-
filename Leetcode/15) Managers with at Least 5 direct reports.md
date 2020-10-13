Difficulty: Medium

[Link to Question](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/)

-------------------------------------

MANAGER WITH ATLEAST 5 DIRECT REPORTS

-------------------------------------

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
```
+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
```
**Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:**
```
+-------+
| Name  |
+-------+
| John  |
+-------+
```
Note:
No one would report to himself.


**Solution:**
```
SELECT NAME FROM Employee
WHERE NAME IN 
( 
SELECT m.NAME
FROM EMPLOYEE e JOIN EMPLOYEE m
ON e.MANAGERID=m.ID
WHERE (m.ID = e.MANAGERID)
GROUP BY m.NAME
HAVING count(m.name) > 4
)
```
OR

```
select Name
from Employee
where id in
   (select ManagerId
    from Employee
    group by ManagerId
    having count(1) >= 5)
```
