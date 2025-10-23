INSERT INTO posts_tags_junct (post_id, tag_id)
SELECT
    p.id AS post_id,
    t.id AS tag_id
FROM
    raw_blog_data r
INNER JOIN
    posts p ON r.post_title = p.title  
INNER JOIN
    tags t ON r.tag_name = t.name      
GROUP BY
    p.id, t.id;                      