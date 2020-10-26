Difficulty: Easy  
[Link to Question](https://leetcode.com/problems/consecutive-available-seats)

------------------------------------------------------

Several friends at a cinema ticket office would like to reserve consecutive available seats.  
**Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?**
```
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
```
Your query should return the following result for the sample case above.
```
| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
```
Note:

    The seat_id is an auto increment int, and free is bool (‘1’ means free, and ‘0’ means occupied.).  
    Consecutive available seats are more than 2(inclusive) seats consecutively available.


**Solution:**
```
SELECT DISTINCT t1.seat_id
FROM cinema AS t1 join cinema AS t2
ON abs(t1.seat_id-t2.seat_id)=1
WHERE t1.free='1' and t2.free='1'
ORDER BY t1.seat_id
;
```
