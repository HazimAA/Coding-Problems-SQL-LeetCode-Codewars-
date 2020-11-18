Difficulty: Medium  
[Link to Question](https://leetcode.com/problems/exchange-seats/)
-------------------------------------

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.  
The column id is continuous increment.

 
Mary wants to change seats for the adjacent students.

 
**Can you write a SQL query to output the result for Mary?**

 
```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
```
For the sample input, the output is:

 
```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
```
Note:  
If the number of students is odd, there is no need to change the last one's seat.

**Solution** 
```
SELECT id, NVL(
                CASE WHEN MOD(id,2) = 1 THEN LEAD(student,1) OVER(ORDER BY id)
                ELSE LAG(student,1) OVER(ORDER BY id)
                END
                ,student
                ) student
FROM seat;
```
