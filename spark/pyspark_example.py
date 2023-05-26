from pyspark.sql import SparkSession

# 建立一個 SparkSession
spark = SparkSession.builder \
    .appName('create-user-table') \
    .master('local[*]') \
    .config('spark.executor.memory', '2g') \
    .config('spark.executor.cores', '2') \
    .getOrCreate()

# builder方法返回Builder物件，用於設定spark的參數，並建立一個SparkSession物件
# 建立session名稱
# 使用本地的所有cpu資源
# 設定executor的資源
# 如果同名session則回傳該session，若無則建立新的session

# 創建一個 Python 列表，其中包含我們想要添加到 DataFrame 中的數據
data = [("Alice", 25, "New York"),
        ("Bob", 30, "Chicago"),
        ("Charlie", 35, "Los Angeles")]

# 建立一個 PySpark DataFrame
df = spark.createDataFrame(data, ['name', 'age', 'city'])
df.show(3, False)

# 插入新數據
df = df.union(spark.createDataFrame([("David", 27, "Chicago"), ("Ella", 24, "New York")], ["name", "age", "city"]))

# 取得城市平均年齡，並按照字母排序
city_mean_age = df \
    .select(['city', 'age']) \
    .groupBy('city') \
    .agg(
        F.avg('age').alias('mean_age'),
        F.count('*').alias('population')) \
    .orderBy('mean_age', ascending=False)


city_mean_age.show()