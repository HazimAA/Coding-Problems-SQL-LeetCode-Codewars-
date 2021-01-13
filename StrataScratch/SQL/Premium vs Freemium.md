[Link to Question](https://platform.stratascratch.com/coding-question?id=10300&python=)
------------------------------------------

Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying customers have more downloads than paying customers. The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.

**SOLUTION**
```
SELECT * FROM
(
  SELECT d.date, 
  SUM(CASE WHEN a.paying_customer = 'no' THEN d.downloads END) non_paying, 
  SUM(CASE WHEN a.paying_customer = 'yes' THEN d.downloads END) paying 
  from ms_user_dimension u
  LEFT JOIN ms_download_facts d
  ON u.user_id = d.user_id
  LEFT JOIN ms_acc_dimension a
  ON u.acc_id = a.acc_id
  GROUP BY d.date
  ORDER BY d.date
) t
WHERE non_paying > paying;
```
