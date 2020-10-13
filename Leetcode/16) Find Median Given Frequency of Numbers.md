Difficulty: Hard

[Link to Question](https://leetcode.com/problems/find-median-given-frequency-of-numbers/)

-----------------------------------------------------------------

The Numbers table keeps the value of number and its frequency.
```
+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
```
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.
```
+--------+
| median |
+--------|
| 0.0000 |
+--------+
```
**Write a query to find the median of all numbers and name the result as median.**


**Solution:**
```
--TO GET CUMULATIVE SUM, NOW WE CAN CHECK EVEN/ODD SUM

SELECT avg(Numberz) FROM
(
SELECT N.*,
SUM(Frequency) OVER 
(
ORDER BY Numberz
) sum_of_frequency,
SUM(Frequency) OVER
() cnt
FROM Numbers N
)
WHERE cnt <= 2 * sum_of_frequency AND
cnt >= 2 * (sum_of_frequency - frequency) 

--EVEN, median should be where the cnt = even will have two values : (n/2) and (n/2)+1 . Avg of these 2 ought to be taken
--ODD,  median should be where the cnt = odd will have one value: n+1/2
--WHERE clause ensures that the output will fit in a particular number entry. First where clause ensures the number fits into ending frequency of the number.
--The Second WHERE clause is to ensure that the median value fits into the starting frequency of the particular number.

--Both the WHERE Clauses work together to give the numbers that would be satisfied. If answer is even, there could be two numbers. 
```

OR

```
select avg(t3.Number) as median
from Numbers as t3 
inner join 
    (select t1.Number, 
        abs(sum(case when t1.Number>t2.Number then t2.Frequency else 0 end) -
            sum(case when t1.Number<t2.Number then t2.Frequency else 0 end)) as count_diff
    from numbers as t1, numbers as t2
    group by t1.Number) as t4
on t3.Number = t4.Number
where t3.Frequency>=t4.count_diff
```
