[Link to Question](https://platform.stratascratch.com/coding-question?id=10308&python=)
---------------------------------------------------------------------------------------

Write a query that calculates the difference between the highest salaries across the marketing and engineering departments. Output just the difference in salaries.

**SOLUTION**
```
SELECT MAX(salary) - MIN(salary) as salary_difference FROM (
SELECT db_dept.department, MAX(db_employee.salary) as salary
FROM db_employee
JOIN db_dept ON db_employee.department_id = db_dept.id
WHERE db_dept.department IN ('engineering','marketing')
GROUP BY db_dept.department
ORDER BY MAX(db_employee.salary) DESC
) t
;
```

OR

```
select max(case when lower(department) like '%marketing%' then salary end)-max(case when lower(department) like '%engineering%' then salary end) as salary_difference
from db_employee
right join db_dept d on d.id=department_id
;
```
