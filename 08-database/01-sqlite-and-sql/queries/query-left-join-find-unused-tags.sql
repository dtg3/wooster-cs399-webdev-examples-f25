SELECT
    t.name AS UnusedTag,
	ptj.tag_id as JunctionID
FROM
    tags t
LEFT JOIN
    posts_tags_junct ptj ON t.id = ptj.tag_id
WHERE
    ptj.tag_id IS NULL;