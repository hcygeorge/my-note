
## 時間函數
mysql
```
date_format(date,'%Y-%m-%d')
str_to_date(date,'%Y-%m-%d')
date_add(s1.first_date, interval 1 day)  # 加一天
```

oracle
```
to_char(visit_date,'YYYY-MM')
to_date()
```

# 計算不重複個數
myslq
```
select COUNT(DISTINCT col_a)
from table_name
group by col_b;
```

## 條件敘述
常會忘記加end
```
case when state = 'approved' then 1 else 0 end
```