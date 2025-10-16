-- Find posts that are linked to two *specific* tags.
-- This requires two separate joins to the post_tag/tag tables.

SELECT
    p.title AS PostTitle
FROM
    posts p
INNER JOIN
    posts_tags_junct pt_tag1 ON p.id = pt_tag1.post_id
INNER JOIN
    tags t_tag1 ON pt_tag1.tag_id = t_tag1.id
INNER JOIN
    posts_tags_junct pt_tag2 ON p.id = pt_tag2.post_id
INNER JOIN
    tags t_tag2 ON pt_tag2.tag_id = t_tag2.id
WHERE
    t_tag1.name = 'WebDev'
    AND t_tag2.name = 'DataScience'
GROUP BY
    p.title; -- Grouping ensures each title appears only once