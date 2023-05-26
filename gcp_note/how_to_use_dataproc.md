# 如何使用dataproc

## 上傳pyspark程式到
gs://pchome-hadoopincloud-codes/eccronj/home/webuser/htdocs/projects/user_portrait

## 上傳並測試執行bash腳本
sudo chmod a+rwx /home/ching_yun/user_portrait.sh
bash /home/ching_yun/user_portrait.sh
cat /home/tmp/projects/user_portrait_log/20221118_user_portrait_log.txt

##
消除window系統在每行結尾留下的'\r'
```bash
sed -i 's/\r$//' /home/webuser/htdocs/projects/search/v2.1/LTR/get_pairwise_data.sh
```