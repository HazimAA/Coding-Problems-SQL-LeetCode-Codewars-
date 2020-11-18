Difficulty: Hard  
[Link to Question](https://leetcode.com/problems/user-purchase-platform/)
-----------------------------------------

(Full Disclaimer, I haven't tested this solution with LeetCode Premium. Would be great if someone could test and let me know if it runs without any hitches.)  

Table: Spending
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| spend_date  | date    |
| platform    | enum    | 
| amount      | int     |
+-------------+---------+
```
The table logs the spendings history of users that make purchases from an online shopping website which has a desktop and a mobile application.
(user_id, spend_date, platform) is the primary key of this table.  
The platform column is an ENUM type of ('desktop', 'mobile').

**Write an SQL query to find the total number of users and the total amount spent using mobile only, desktop only and both mobile and desktop together for each date.**

The query result format is in the following example:

Spending table:
```
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+
```
Result table:
```
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+ 
```
On 2019-07-01, user 1 purchased using both desktop and mobile, user 2 purchased using mobile only and user 3 purchased using desktop only.  
On 2019-07-02, user 2 purchased using mobile only, user 3 purchased using desktop only and no one purchased using both platforms.


**Solution:**
```
-- FOR MOBILE AND DESKTOP
SELECT t1.spend_date, 'both' as platform, sum(nvl(t.total_amount, 0)) as total_amount, count(t.user_id) as total_users
from
(   --SUM OF AMOUNT WHERE BOTH PLATFORMS ARE USED
    SELECT user_id, spend_date, sum(amount) as total_amount
    FROM spending
    GROUP BY user_id, spend_date
    HAVING COUNT(platform) = 2
    ORDER BY spend_date, user_id
) t
--JOINING TO GET AMOUNT AS 0 FOR DATES WHERE 'BOTH' WERENT USED
RIGHT JOIN (SELECT DISTINCT spend_date FROM spending) t1
ON t.spend_date = t1.spend_date
GROUP BY t1.spend_date

UNION
-- FOR MOBILE ONLY
SELECT t2.spend_date, 'mobile' as platform, sum(nvl(t.amount, 0)) as total_amount, count(t.user_id) as total_users
FROM
(
    SELECT user_id, spend_date, amount
    FROM spending
    WHERE user_id IN (
        --Obtaining users who have used only one platform
        SELECT Distinct user_id from (
            SELECT user_id, spend_date
            FROM spending
            GROUP BY user_id, spend_date
            HAVING COUNT(platform) <2
            ORDER BY spend_date, user_id
        )
    ) 
    AND platform = 'mobile'
    ORDER BY spend_date, user_id
) t
RIGHT JOIN (SELECT DISTINCT spend_date FROM spending) t2
ON t.spend_date = t2.spend_date
GROUP BY t2.spend_date

UNION
-- FOR DESKTOP ONLY
SELECT t3.spend_date, 'Desktop' as platform, sum(nvl(t.amount, 0)) as total_amount, count(t.user_id) as total_users
FROM
(
    SELECT user_id, spend_date, amount
    FROM spending
    WHERE user_id IN (
        --Obtaining users who have used only one platform
        SELECT Distinct user_id from (
            SELECT user_id, spend_date
            FROM spending
            GROUP BY user_id, spend_date
            HAVING COUNT(platform) <2
            ORDER BY spend_date, user_id
        )
    ) 
    AND platform = 'desktop'
    ORDER BY spend_date, user_id
) t
RIGHT JOIN (SELECT DISTINCT spend_date FROM spending) t3
ON t.spend_date = t3.spend_date
GROUP BY t3.spend_date
;
```
