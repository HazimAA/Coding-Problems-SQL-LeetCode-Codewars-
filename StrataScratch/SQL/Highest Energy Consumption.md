Difficulty: Medium  
[Link to Question](https://platform.stratascratch.com/coding-question?id=10064&python=)  
---------------------------------------------------------------------------------
  
**Find the date with the highest total energy consumption from the Facebook data centers.** Output the date along with the total energy consumption across all data centers.

**Solution:** 
```
SELECT t.date, SUM(t.consumption) FROM
(
select * from 
fb_eu_energy UNION ALL

select * from
fb_asia_energy UNION ALL

select * from
fb_na_energy
) as t
GROUP BY t.date
ORDER BY SUM(t.consumption) DESC
LIMIT 2;
```
