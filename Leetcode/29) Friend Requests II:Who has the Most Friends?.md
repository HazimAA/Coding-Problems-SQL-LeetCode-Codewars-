Difficulty: Medium  
[Link to Question](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/)

-------------------------------------

In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well.
Table request_accepted holds the data of friend acceptance, while requester_id and accepter_id both are the id of a person.

```
| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
```

**Write a query to find the the people who has most friends and the most friends number. For the sample data above, the result is:**
```
| id | num |
|----|-----|
| 3  | 3   |
```
Note:

    It is guaranteed there is only 1 people having the most friends.
    The friend request could only been accepted once, which mean there is no multiple records with the same requester_id and accepter_id value.

Explanation:
The person with id ‘3’ is a friend of people ‘1’, ‘2’ and ‘4’, so he has 3 friends in total, which is the most number than any others.

**Solution**
```
SELECT SENT_BY, SUM(COUNT_OF_SENT)
FROM
    (
    SELECT sender_id as sent_by, COUNT(sender_id) as Count_of_Sent
    FROM friend_request
    GROUP BY sender_id
    
    UNION
    
    SELECT send_to_id as accepted_by, COUNT(send_to_id) as Count_of_Accepted
    FROM friend_request
    GROUP BY send_to_id
    )
GROUP BY SENT_BY
ORDER BY SUM(COUNT_OF_SENT) DESC
FETCH FIRST ROW ONLY
```
