#%%
import pandas as pd
import numpy as np

#%% 載入資料集：將資料集以 DataFrame 的形式載入到 Pandas 中，並命名為 df。
student = pd.read_csv('../data/pandas_example_student01.csv', sep=',')
student2 = pd.read_csv(
    '../data/pandas_example_student02.csv',
    sep=',',
    names=['姓名', '科目', '成績']
    )
test_time = pd.read_csv(
    '../data/pandas_example_testtime.csv',
    sep=','
    )

#%% 查看前五筆資料：顯示 df 的前五筆資料。
student.head()
# student.dtypes

#%% 排序資料：將 df 按照「姓名」和「科目」欄位進行升序排序。
student.sort_values(['姓名', '科目'], ascending=True)

#%% 聚合操作：計算每個學生的總成績，並將結果存儲在一個新的欄位「總分」中。
# student \
#     .groupby(['姓名'])['成績', '科目'] \
#     .agg(
#         總分=('成績', 'sum'),
#         科目數=('科目', 'nunique')
#          )

student \
    .groupby(['姓名'])['成績', '科目'] \
    .agg({'成績': 'sum', '科目': 'nunique'}) \
    .rename(columns={'成績': '總分', '科目': '考幾科'})  # 注意一定要加columns

#%% 遺漏值處理：將資料集中的所有遺漏值（如果有的話）填充為 0。
student.fillna({'成績': 0, '科目': 'Science'})

#%% 合併資料集：創建一個新的 DataFrame df2，包含學生姓名和性別兩個欄位。將 df 和 df2 按照學生姓名進行合併。
union_df = pd.concat([student, student2], ignore_index=True)
union_df

#%% 重塑資料：將 df 轉換成以「姓名」為索引，「科目」為欄位的形式
student \
    .fillna({'科目': 'Science'}) \
    .drop_duplicates() \
    .pivot(index='姓名', columns='科目') \


#%% 時間序列處理：假設我們有一個包含日期和學生考試時間的資料集，將其加入到 df 中，並將日期設置為索引。
test_time['日期'] = pd.to_datetime(test_time['日期'], format='%Y-%M-%d')
test_time

#%% 合併成績與考試科目圖
student.merge(test_time, how='left', on=['姓名', '科目'])

#%% 可視化：使用 df 中的數據繪製每個學生的成績折線圖。
