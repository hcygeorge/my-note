# 定義如何將GCS數據傳到BQ
function gcs2bq() {
    TARGET_PROJECT_ID=bigdata-datateamcloud
    DATASET=user_portrait
    TABLE=$1
    BUCKET_NAME=pchome-hadoopincloud-hadoop/projects/Gaia/member/user_portrait/$2
    PREFIX=part
    bq load --replace=true --project_id=${TARGET_PROJECT_ID} --source_format=PARQUET ${DATASET}.${TABLE} "gs://${BUCKET_NAME}/${PREFIX}*.parquet"
}


gcs2bq "member" "member/v1/parquet/current"


# 建立table(記得project和dataset中間是冒號)
bq mk -t \
--schema /path/to/schema.json \
project_id:dataset_id.table_id