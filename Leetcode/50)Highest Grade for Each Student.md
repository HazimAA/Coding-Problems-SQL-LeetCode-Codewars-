Difficulty: Medium  
[Link to Question](https://leetcode.com/problems/highest-grade-for-each-student/)
-----------------------------------------------------------

Table: Enrollments
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) is the primary key of this table.
```

**Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id. The output must be sorted by increasing student_id.**

The query result format is in the following example:

Enrollments table:
```
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+
```
Result table:
```
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
```

**Solution:**
```
SELECT STUDENT_ID, MIN(COURSE_ID) AS COURSE_ID, GRADE
FROM ENROLLMENTS
WHERE (STUDENT_ID, GRADE) IN
(
SELECT STUDENT_ID, MAX(GRADE)
FROM ENROLLMENTS
GROUP BY STUDENT_ID
)
GROUP BY STUDENT_ID, GRADE
ORDER BY STUDENT_ID ASC
```

OR

```
SELECT STUDENT_ID, COURSE_ID, GRADE
FROM
(
    SELECT student_id, course_id, grade, row_number() OVER (
    PARTITION BY student_id
    ORDER by student_id ASC, GRADE DESC, course_id
    ) AS ranked_grades
    FROM Enrollments
)
WHERE ranked_grades = 1
```
