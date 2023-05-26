-- 建立一個包含註冊日期和用戶ID的CTE，作為計算基礎
WITH cohort_base AS (
  SELECT
    registration_date, -- 註冊日期
    user_id            -- 用戶ID
  FROM
    member             -- 來源表格：member
),

-- 建立一個用於計算註冊人數、註冊後第1天和第2天活躍用戶數的CTE
cohorts AS (
  SELECT
    cb1.registration_date, -- 註冊日期
    COUNT(DISTINCT cb1.user_id) AS registration_count, -- 註冊人數
    -- 註冊後第1天活躍用戶數
    COUNT(DISTINCT CASE WHEN DATEDIFF(day, cb1.registration_date, m.activity_date) = 1 THEN cb1.user_id END) AS day1_active_users,
    -- 註冊後第2天活躍用戶數
    COUNT(DISTINCT CASE WHEN DATEDIFF(day, cb1.registration_date, m.activity_date) = 2 THEN cb1.user_id END) AS day2_active_users
  FROM
    cohort_base cb1
    JOIN member m ON cb1.user_id = m.user_id -- 連接基礎CTE與member表格
  GROUP BY
    cb1.registration_date -- 依註冊日期進行分組
)

-- 計算留存率並按註冊日期排序
SELECT
  registration_date,
  registration_count,
  day1_active_users * 1.0 / registration_count AS retention_day1, -- 註冊後第1天留存率
  day2_active_users * 1.0 / registration_count AS retention_day2  -- 註冊後第2天留存率
FROM
  cohorts
ORDER BY
  registration_date; -- 按註冊日期排序