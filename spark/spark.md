# QA

## 比較DataFrame與RDD

TL,DR: Spark DataFrame具有統一的Schema，因此只需要在整個DataFrame中存儲一次Schema，可以減少記憶體使用，RDD則是每個元素都可以是不同的類型，需要額外的代碼來處理不同類型的資料元素，因此現在基本上都鼓勵使用dataframe而非RDD。

Spark DataFrame具有統一的Schema，也就是所有的行都具有相同的列和資料類型。若在序列化和反序列化時，每個資料物件都需要存儲其對應的Schema，那麼處理大量資料時，這些Schema的存儲將變得非常昂貴，並會占用大量記憶體空間。但是，由於Spark DataFrame具有統一的Schema，因此只需要在整個DataFrame中存儲一次Schema，然後在序列化和反序列化時引用即可，這樣可以顯著減少內存使用和磁碟存儲空間的需求。

RDD中的每個元素都可以是不同的類型，例如字典、元組、列表和整數等，並且每個元素也可以具有不同的欄位和資料類型。因此，RDD中的資料結構是不統一的，而且RDD中的元素可以是任意的類型。

與Spark DataFrame不同，RDD沒有統一的Schema，因此在處理和分析RDD資料時，需要額外的代碼來處理不同類型的資料元素，例如進行類型轉換或欄位選擇等操作。這也是為什麼Spark DataFrame比RDD更加方便和易於使用的原因之一。

## transformation和action的差異
transformation函數只定義資料處理的過程，並不會直接計算出答案，所以回傳一個新的RDD或DataFrame。
action類的函數，則會觸發spark的計算，然後回傳計算結果
- collect()
- show(n, False)
- take(n)
- count()
- write().mode('overwrite').options(header=True).parquet('./data/file01.parquet')
- write().mode('overwrite').options(header=True).csv('./data/file01.csv')

## executor
在 Spark 中，executor 是一個執行緒池，負責執行 Spark 應用程式的任務。每個 Spark 執行緒池（即一個 Spark 應用程式）都有自己的 executor，並在工作節點上啟動。在 Spark 中，工作節點（worker node）是一個運行 Spark 的主機，可以擁有多個 executor。

因此，可以這樣說：一個 Spark 應用程式可以由多個 executor 組成，而這些 executor 可以運行在一個或多個工作節點上。在 Spark 中，executor 負責處理應用程式的任務，而工作節點則負責管理和分配 executor 的資源。
