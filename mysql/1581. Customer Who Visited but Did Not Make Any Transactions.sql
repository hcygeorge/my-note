-- join需要逐一比對值，在大量資料下沒有效率
-- in優點是不管找的值有多少，只要掃描整張表一次
-- exist則是每找一個值就要掃描一次，但不用掃描全部的表

SELECT
    v.customer_id,
    count(v.visit_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id

-- 在有大量的visit_id,IN只需要掃描表一次Transactions就能找到所有比對相同的值
SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits
WHERE visit_id NOT IN (
	SELECT visit_id FROM Transactions
	)
GROUP BY customer_id

-- EXIST只需要為每個visit_id掃描一次Transactions，但只要找到第一個對的值就會停止，不需要掃描整張表
SELECT
    v.customer_id,
    count(v.visit_id) as count_no_trans
FROM Visits v
WHERE NOT EXISTS(
    SELECT * FROM Transactions t WHERE v.visit_id = t.visit_id
)
GROUP BY v.customer_id
