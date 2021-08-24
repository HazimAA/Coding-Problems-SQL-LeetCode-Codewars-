Difficulty: Easy  
[Link To Question](https://leetcode.com/problems/reformat-department-table/)  
-----------------------------------------------------------------------------

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The query result format is in the following example:

Department table:
```
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
```
Result table:
```
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
``` 
Note that the result table has 13 columns (1 for the department id + 12 for the months).


**Solution:**  
```
/* Write your PL/SQL query statement below */
select *
from (select id, revenue, month from department)
pivot(
    sum(revenue)
    for month in
    (
        'Jan' as "Jan_Revenue",'Feb' as "Feb_Revenue",'Mar' as "Mar_Revenue",'Apr' as "Apr_Revenue",'May' as "May_Revenue",'Jun' as"Jun_Revenue",'Jul' as "Jul_Revenue",'Aug' as "Aug_Revenue",'Sep' as "Sep_Revenue",'Oct' as "Oct_Revenue",'Nov' as "Nov_Revenue",'Dec' as "Dec_Revenue"
    )
)
order by id
;
```
