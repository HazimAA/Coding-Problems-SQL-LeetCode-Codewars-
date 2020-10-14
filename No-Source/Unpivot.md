This is a table calles GRADES which stores the grade of each student in a subject.

Show a query which results in the name of the student and the average for the 3 classes

BUT ONLY showing students whose average is more than 70.

Name the column for average for the 3 classes AS 'FINAL GRADE'
You cannot use (math + hist + scien)/3 to get the average.


```
GRADES
name	math	hist	scien
Matt	70	80	90
Scott	66	55	25
Ada	88	99	79
Mary	25	55	1
John	88	90	91
```

**Solution**
```
With unpiv as (
SELECT *
from Grades
UNPIVOT
(
Marks FOR score in (math as 'Mathematics', hist as 'history', scien as 'science')
)

)

SELECT Names, AVG(Marks) as avgs
FROM unpiv
GROUP BY Names
HAVING avg(marks) > 70;
```
