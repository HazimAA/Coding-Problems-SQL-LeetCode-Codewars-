Difficulty: Medium

[Link to Question](https://leetcode.com/problems/get-highest-answer-rate-question/)

-----------------------------------------------------------------------------------

**Get the highest answer rate question from a table survey_log with these columns: uid, action, question_id, answer_id, q_num, timestamp.**

uid means user id; action has these kind of values: “show”, “answer”, “skip”;   
answer_id is not null when action column is “answer”,   
while is null for “show” and “skip”; q_num is the numeral order of the question in current session.

Write a sql query to identify the question which has the highest answer rate.

Example:

Input:
```
+------+-----------+--------------+------------+-----------+------------+
| uid  | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
```
Output:
```
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+
```
Explanation:
question 285 has answer rate 1/1, while question 369 has 0/1 answer rate, so output 285.

Note: The highest answer rate meaning is: answer number’s ratio in show number in the same question.

**Solution**
```
SELECT QUESTION_ID as survey_log
FROM
(
SELECT 
question_id,
SUM(CASE WHEN S.ACTION = 'show' THEN 1 ELSE 0 END) AS "The Shown action Count",
SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) AS "The Answer action Count"
FROM SURVEY_LOG S
GROUP BY QUESTION_ID
) as t
ORDER BY "The Answer action Count"/"The Shown action Count" DESC
fetch first row only
```
---- alternate solution--------
```
SELECT QUESTION_ID as survey_log
FROM
(
SELECT 
question_id,
( SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) / SUM(CASE WHEN S.ACTION = 'show' THEN 1 ELSE 0 END) ) AS Rate
-- SUM(CASE WHEN S.ACTION = 'show' THEN 1 ELSE 0 END) AS "The Shown action Count",
-- SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) AS "The Answer action Count"
FROM SURVEY_LOG S
GROUP BY QUESTION_ID
ORDER BY Rate DESC
)
FETCH FIRST ROW ONLY
;
```
