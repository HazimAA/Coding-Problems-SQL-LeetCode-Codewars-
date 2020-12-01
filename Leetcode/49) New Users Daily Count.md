Difficulty: Medium  
[Link to Question](https://leetcode.com/problems/new-users-daily-count/)
------------------------------------------------------------------------

Table: Traffic
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| activity      | enum    |
| activity_date | date    |
+---------------+---------+
```
There is no primary key for this table, it may have duplicate rows.
The activity column is an ENUM type of ('login', 'logout', 'jobs', 'groups', 'homepage').

**Write an SQL query that reports for every date within at most 90 days from today, the number of users that logged in for the first time on that date. Assume today is 2019-06-30.**

The query result format is in the following example:

Traffic table:
```
+---------+----------+---------------+
| user_id | activity | activity_date |
+---------+----------+---------------+
| 1       | login    | 2019-05-01    |
| 1       | homepage | 2019-05-01    |
| 1       | logout   | 2019-05-01    |
| 2       | login    | 2019-06-21    |
| 2       | logout   | 2019-06-21    |
| 3       | login    | 2019-01-01    |
| 3       | jobs     | 2019-01-01    |
| 3       | logout   | 2019-01-01    |
| 4       | login    | 2019-06-21    |
| 4       | groups   | 2019-06-21    |
| 4       | logout   | 2019-06-21    |
| 5       | login    | 2019-03-01    |
| 5       | logout   | 2019-03-01    |
| 5       | login    | 2019-06-21    |
| 5       | logout   | 2019-06-21    |
+---------+----------+---------------+
```
Result table:
```
+------------+-------------+
| login_date | user_count  |
+------------+-------------+
| 2019-05-01 | 1           |
| 2019-06-21 | 2           |
+------------+-------------+
```
Note that we only care about dates with non zero user count.
The user with id 5 first logged in on 2019-03-01 so he's not counted on 2019-06-21.

**Solution**
```
--NUMBER OF USERS THAT LOGGED IN FOR THE FIRST TIME ON A PARTICULAR DATE WITHIN 90 DAYS OF 2019-06-30
SELECT activity_date, COUNT(user_id)
FROM
(   --MASTER TABLE OF USERS AND ACTIVITY DATE, WITH ALL OF THEIR FIRST MONTHLY LOG INS
    SELECT activity_date, user_id, min(activity_date) as first_login_date
    FROM traffic
    GROUP BY activity_date,user_id
    ORDER BY activity_date
)
--FILTERS USERS THAT LOGGED IN BEFORE 90 DAYS FROM PRESENT DATE 2019-06-30
WHERE user_id NOT IN
(
    SELECT user_id
    FROM
        (
            SELECT activity_date, user_id, min(activity_date) as first_login_date
            FROM traffic
            GROUP BY activity_date,user_id
            ORDER BY activity_date
        )
    WHERE to_date('2019-06-30','yyyy-mm-dd') - activity_date >= 90
)
GROUP BY activity_date
```
