Difficulty: Easy  
[Link to Question](https://leetcode.com/problems/shortest-distance-in-a-plane/)
-------------------------------------------------

Question

Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.  
**Write a query to find the shortest distance between these points rounded to 2 decimals.**
```
 x  y
-1 -1
 0  0
-1 -2
```

The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:

```
shortest
1.00
```
Note: The longest distance among all the points are less than 10000.


**Solution**
```
SELECT
ROUND(MIN(SQRT(POWER(P1.X - P2.X, 2) + POWER(P1.Y - P2.Y, 2)))) AS shortest
FROM point_2d p1, point_2d p2
WHERE
P1.X <> P2.X OR
P1.Y <> P2.Y
```
