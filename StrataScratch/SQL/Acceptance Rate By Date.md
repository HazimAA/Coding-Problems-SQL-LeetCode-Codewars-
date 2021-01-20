Difficulty: Medium  
[Link to Question](https://platform.stratascratch.com/coding-question?id=10285&python=)
-----------------------------------------------

What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date the request was sent. Order by the earliest date to latest.

Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.
Table: fb_friend_requests

**Solution:**
```
SELECT s.date, COUNT(a.user_id_receiver)::NUMERIC/COUNT(s.user_id_sender) AS percentage_acceptance FROM
  (
  SELECT date, user_id_sender, user_id_receiver
  FROM fb_friend_requests
  WHERE action = 'sent'
  ) s
LEFT JOIN 
  (
  SELECT date, user_id_sender, user_id_receiver
  FROM fb_friend_requests
  WHERE action = 'accepted'
  ) a
ON
s.user_id_sender = a.user_id_sender AND
s.user_id_receiver = a.user_id_receiver
GROUP BY s.date
;
```
