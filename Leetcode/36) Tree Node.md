Difficulty: Medium  
[Link to Question](https://leetcode.com/problems/tree-node/)

---------------------------------

Given a table tree, id is identifier of the tree node and p_id is its parent node’s id.
```
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
```
Each node in the tree can be one of three types:

    Leaf: if the node is a leaf node.  
    Root: if the node is the root of the tree.  
    Inner: If the node is neither a leaf node nor a root node.  

**Write a query to print the node id and the type of the node. Sort your output by the node id. The result for the above sample is:**
```
+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
```
Explanation

    Node ‘1’ is root node, because its parent node is NULL and it has child node ‘2’ and ‘3’.  
    Node ‘2’ is inner node, because it has parent node ‘1’ and child node ‘4’ and ‘5’.  
    Node ‘3’, ‘4’ and ‘5’ is Leaf node, because they have parent node and they don’t have child node.  

And here is the image of the sample tree as below:  
```
        1  
      /   \  
    2       3
  /   \
4       5
```

Note

If there is only one node on the tree, you only need to output its root attributes.

**Solution**

```
select id, 'ROOT' as Type from tree
where p_id is null
union
select id,'Leaf' as Type from tree
where id not in (select p_id from tree where p_id is not null)
union
select id, 'Inner' as Type from tree
where id in (select p_id from tree where p_id is not null)
and p_id is not null
```

OR

ALTERNATE (NOT TESTED FOR ALL CASES)

```
SELECT id, 'Root' as Type
FROM tree
where p_id is null

UNION

SELECT id, 'Inner' as Type
FROM tree 
WHERE p_id IN (SELECT id FROM tree where p_id is null) --only includes the entries that arise from the root node
AND id IN (SELECT DISTINCT p_id FROM tree) --removes the entries that are not a parent 

UNION 

SELECT id, 'Leaf' as Type
FROM tree
WHERE id NOT IN (SELECT p_id FROM tree WHERE p_id IS NOT NULL)

ORDER BY id
;
```
