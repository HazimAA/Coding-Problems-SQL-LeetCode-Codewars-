[Link to Question](https://platform.stratascratch.com/coding-question?id=10309&python=)
---------------------------------------------------------------------------------------

You have a table of in-app purchases by user. Users that make their first in-app purchase are placed in a marketing campaign where they see call-to-actions for more in-app purchases. Find the number of users that made additional in-app purchases due to the success of the marketing campaign.



The marketing campaign doesn't start until one day after the initial in-app purchase so users that make multiple purchases on the same day do not count, nor do we count users that make only the same purchases over time. To simplify the scenario, consider users that order multiple products on day 1 and then purchase one of those products in the future as beneficiaries of the marketing campaign (e.g., count users who orders product IDs 1, 2, 3 on day 1 and then orders only product id 1 a few days later).


**SOLUTION**
```
select count(*) as user_count from
(
select user_id, count(distinct created_at) as days_when_purchased, count(distinct product_id) as no_of_prods_purchased
from marketing_campaign
GROUP BY user_id
) t
where days_when_purchased > 1 
and no_of_prods_purchased > 1
;
```
