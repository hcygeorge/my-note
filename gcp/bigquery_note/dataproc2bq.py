def save_table(self, spark_df, table_id, temp_bucket='pchome-hadoopincloud-hadoop-dev'):
    """Save spark dataframe to BigQuery"""
    client = bigquery.Client(project=table_id.split('.')[0])

    spark_df.write.format('bigquery') \
        .option('table', table_id) \
        .option('temporaryGcsBucket', temp_bucket) \
        .mode('overwrite') \
        .save()