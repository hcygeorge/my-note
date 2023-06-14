
-- tips: 選取的欄位不含primary key，可能會有重複，使用distinct()

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id asc