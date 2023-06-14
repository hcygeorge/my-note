-- Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.

-- tips: 不等於條件不會列出Null值，需要加is null

SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS Null