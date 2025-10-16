SELECT
    p.title AS PostTitle,
    t.name AS TagName,
    a.username AS Author
FROM
    posts p
INNER JOIN
    users a ON p.author_id = a.id
INNER JOIN
    posts_tags_junct ptj ON p.id = ptj.post_id
INNER JOIN
    tags t ON ptj.tag_id = t.id
WHERE
    p.title = 'Designing Clean Database Schemas'