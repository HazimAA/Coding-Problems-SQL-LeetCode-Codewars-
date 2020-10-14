Difficulty: Hard  
[Link to Question](https://leetcode.com/problems/human-traffic-of-stadium/)

-----------------------------------

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the primary key for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
No two rows will have the same visit_date, and as the id increases, the dates increase as well.
```
 

**Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.**

Return the result table ordered by visit_date in ascending order.

The query result format is in the following example.

```
Stadium table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
```
```
Result table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
```
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.

**Solution**
```
With tabibitosan as
(
/* This outer query is the Tabibitosan query, which groups the consecutive 
dates together by performing a simple subtraction of (id and row number) 
between consecutive rows */

SELECT Id, visit_date, people, 
row_number() OVER (order by id) rn, 
id - row_number() OVER (order by id) grp
    FROM (
	
		/* This subquery picks out the Data where No of People >= 100 */
		
        SELECT s.* FROM stadium s WHERE s.id NOT IN (
        SELECT id 
        FROM stadium 
        WHERE people < 100
        )
        ORDER BY visit_date
    )
)

/* We take a count of the number of entries in the grp column generated in the cte. 
We filter for those rows where the consecutive values are >= 3, as required by 
the question */

SELECT id as id, to_char(visit_date, 'YYYY-MM-DD') as visit_date, people as people FROM (
SELECT id, visit_date, people, count(1) OVER (PARTITION BY grp) pt
FROM tabibitosan 
)
WHERE pt >= 3
ORDER BY ID
```
