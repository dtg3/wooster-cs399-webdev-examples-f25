SELECT
    t.name AS TagName,
    COUNT(ptj.post_id) AS NumberOfPosts
FROM
    tags t
INNER JOIN
    posts_tags_junct ptj ON t.id = ptj.tag_id
GROUP BY
    t.name
HAVING
    COUNT(ptj.post_id) > 1
ORDER BY
    NumberOfPosts DESC, TagName ASC;