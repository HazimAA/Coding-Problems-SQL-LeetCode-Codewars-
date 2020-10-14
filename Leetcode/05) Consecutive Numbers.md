**Write a SQL query to find all numbers that appear at least three times consecutively.**

Difficulty: Medium

[Link to Question](https://leetcode.com/problems/consecutive-numbers/)

```
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
```

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

```
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
```


**Solution**

```
SELECT DISTINCT l1.Num  ConsecutiveNums
/* Using Distinct since the question doesn't specify what to do if a number occurs 4 times in a row. If I don't use Distinct, it will the output value twice. Ex: For input 1,1,1,1--- the soln would be (1,1) since 1 occurs consecutively 3 times, twice in the input sequence */
FROM 
  Logs l1,
  Logs l2,
  Logs l3        

WHERE
      l1.Id = l2.Id + 1 
      AND l2.Id= l3.Id +1
      AND l1.Num =l2.Num
      AND l2.Num = l3.Num
    ;
```
