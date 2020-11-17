Diffiulty: Hard  
[Link to Question](https://leetcode.com/problems/average-salary-departments-vs-company/)
------------------------------------------------------------

**Given two tables as below, write a query to display the comparison result (higher/lower/same) of the average salary of employees in a department to the company’s average salary.**

Table: salary
```
| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |
```
The employee_id column refers to the employee_id in the following table employee.
```
| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |
```
So for the sample data above, the result is:
```
| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |
```
Explanation  
In March, the company’s average salary is (9000+6000+10000)/3 = 8333.33…
The average salary for department ‘1’ is 9000, which is the salary of employee_id ‘1’ since there is only one employee in this department. So the comparison result is ‘higher’ since 9000 > 8333.33 obviously.
The average salary of department ‘2’ is (6000 + 10000)/2 = 8000, which is the average of employee_id ‘2’ and ‘3’. So the comparison result is ‘lower’ since 8000 < 8333.33.
With he same formula for the average salary comparison in February, the result is ‘same’ since both the department ‘1’ and ‘2’ have the same average salary with the company, which is 7000.

**Solution**
```
SELECT t1.Month, t2.Department_id,
CASE
    WHEN t2.Department_Average > t1.Monthly_Average THEN 'Higher'
    WHEN t2.Department_Average = t1.Monthly_Average THEN 'Same'
    WHEN t2.Department_Average < t1.Monthly_Average THEN 'Lower'
END Comparison
FROM

    --Monthly Company Average
    (SELECT TO_CHAR(PAY_DATE,'YYYY-MM') as Month, ROUND(AVG(AMOUNT),2) AS Monthly_Average
    FROM Salary
    GROUP BY PAY_DATE
    ORDER BY PAY_DATE DESC
    ) t1
   
    INNER JOIN
   
    --Monthly Department Average
    (SELECT DISTINCT e.department_id, TO_CHAR(s.PAY_DATE,'YYYY-MM') as Month, AVG(s.AMOUNT) as Department_Average
    FROM salary s JOIN employee e
    ON e.employee_id = s.employee_id
    GROUP BY e.department_id, s.PAY_DATE
    ORDER BY Month DESC
    ) t2
    on t1.Month = t2.Month
```
