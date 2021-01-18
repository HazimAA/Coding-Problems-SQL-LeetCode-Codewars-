Difficulty: Medium  
[Link to Question](https://platform.stratascratch.com/coding-question?id=10288&python=)
---------------------------------------------------------------

You're given a table that contains search results. If the 'position' column represents the position of the search results, write a query to calculate the percentage of search results that were in the top 3 position.

**SOLUTION:**
```
SELECT (COUNT(CASE WHEN position < 4 THEN 1 ELSE NULL END) * 100)::NUMERIC/COUNT(*) AS top_3_percentage
FROM fb_search_results
;
```
