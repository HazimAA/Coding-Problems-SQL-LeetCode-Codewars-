Difficulty: Hard  
[Link to Question](https://platform.stratascratch.com/coding-question?id=10284&python=)
----------------------------------------------------------------------------------------

Popularity Percentage  
**Find the popularity percentage for each user on Facebook.** The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, then converted into a percentage by multiplying by 100.
Output each user along with their popularity percentage. Order records in ascending order by user id.
The 'user1' and 'user2' column are pairs of friends.

**SOLUTION:**
```
Select user1, count(user2)*100.0/count(*)over() as popularity_percent
from (
    Select user1, user2
    from facebook_friends
    union
    Select user2 as user1, user1 as user2
    from facebook_friends) as a
group by 1
order by 1
```

or

```
SELECT t2.user1, 
count(t2.user2)*100::NUMERIC/t.total_users as popularity_percentage
FROM
    (
    SELECT COUNT(a.user1) as total_users
    FROM
        (
        SELECT user1 from facebook_friends
        UNION
        SELECT user2 from facebook_friends
        order by user1
        ) a
    ) t
 JOIN 
    (
    SELECT user1, user2
    FROM facebook_friends
    UNION
    SELECT user2, user1
    FROM facebook_friends
    ) t2
ON 1=1
GROUP BY t2.user1, t.total_users
ORDER BY t2.user1, t.total_users
;
```
