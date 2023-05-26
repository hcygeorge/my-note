-- 排除特定欄位
SELECT DISTINCT * EXCEPT (user_mail) FROM `bigdata-datateamcloud.user_portrait.summary` LIMIT 1000;

-- 抽樣(只能對實體表)
SELECT * FROM dataset.my_table TABLESAMPLE SYSTEM (10 PERCENT)
