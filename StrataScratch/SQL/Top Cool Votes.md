Difficulty: Medium  
[Link to Question](https://platform.stratascratch.com/coding-question?id=10060&python=) 
--------------------------------------------------------------------------------------------

Find the business and the review_text that received the highest number of  'cool' votes.

Output the business name along with the review text.

**Solution**  
```
SELECT business_name, review_text
FROM yelp_reviews
ORDER BY cool DESC
LIMIT 2;
```

