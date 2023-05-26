# 如何使用Python串接BQ

若在本機開發，除了安裝GCP SDK外，需先在 GCP 上設定好憑證，下載服務帳戶的金鑰 (key) 的步驟如下：

1. 前往 Google Cloud Console 網站，並登入您的帳戶。
2. 選擇您想要下載金鑰的專案 (project)。
3. 點選左側導覽列中的「IAM 和管理」(IAM & Admin)。
4. 點選頁面上方的「服務帳戶」(Service accounts)。
5. 選擇您要下載金鑰的服務帳戶。
6. 在金鑰區塊中，點選「建立金鑰」(Create Key)。
7. 選擇金鑰的類型 (JSON 或 P12)，JSON 格式是最常用的，因為它容易讀取和編寫。
8. 下載金鑰後，將其儲存在安全的地方，例如您的本機端電腦上。
9. 請務必妥善保管金鑰，並確保不要將其公開或分享給其他人。
10. 完成上述步驟後，您就可以將下載的金鑰儲存在本機端，並在程式碼中使用該金鑰來設定認證憑證，以便使用 BigQuery 服務。

```python
from google.cloud import bigquery

# 設定認證憑證路徑，需先在 GCP 上設定好
service_account_json = '/path/to/service_account.json'

# 建立 BigQuery 客戶端
client = bigquery.Client.from_service_account_json(service_account_json)

# 撰寫 SQL 查詢語句
query = """
SELECT *
FROM `project.dataset.table`
"""
query_job = client.query(query)
results = query_job.result()
for row in results:
    print(row)
```

如果使用GCP的VM開發，VM會自動檢查VM服務帳戶的憑證，無需自行設定
```python
from google.cloud import bigquery
client = bigquery.Client()

# 建立 BigQuery 客戶端
client = bigquery.Client.from_service_account_json(service_account_json)

# 撰寫 SQL 查詢語句
query = """
SELECT *
FROM `project.dataset.table`
"""
query_job = client.query(query)
results = query_job.result()
for row in results:
    print(row)
```

用pandas讀取Big Query數據

```python
from google.cloud import bigquery
import pandas as pd

# 創建 BigQuery 客戶端
client = bigquery.Client()

# 構建 SQL 查詢
query = """
SELECT *
FROM `bigdata-datateamcloud.user_portrait.member`
LIMIT 10000
"""

df = pd.read_gbq(query=query, dialect='standard')
```