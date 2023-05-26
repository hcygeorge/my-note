# sudo pip3 install google-cloud-bigquery
# sudo pip3 install pandas_gbq
from google.cloud.bigquery import Client
import pandas as pd
import textwrap

class BigQueryLoader():
    """A class to load data from BigQuery tables."""
    
    def __init__(self):
        self.database_id = 'bigdata-datateamcloud.user_portrait'
        self.col_names = {
            'summary': [
                'uid','gender','birth','age','zip',
                'gender_pred', 'is_edm_ok','is_company',
                'last_login', 'rfm_new',
                'ROUND(IFNULL(avgprice, 0), 2) as avgprice',
                'IFNULL(cnt_item, 0) as cnt_item',
            ],
            'main_indicator': [
                "COUNT(1) AS num_user",
                "AVG(avgprice) AS avgprice",
                "AVG(cnt_item) AS cnt_item",
                "SUM(CASE WHEN gender='M' THEN 1 ELSE 0 END) AS num_male",
                "SUM(CASE WHEN gender='F' THEN 1 ELSE 0 END) AS num_female",
                "SUM(CASE WHEN is_edm_ok THEN 1 ELSE 0 END) AS is_edm_ok",
                "SUM(CASE WHEN is_company THEN 1 ELSE 0 END) AS is_company",
            ]
        }
        
        self.col_values = {
            'rfm_new': [
                '未貼標', '活躍_低價值', '流失_低價值',
                '未轉換', '活躍_中價值', '活躍_高價值',
                '待喚回_高價值', '新客', '舊客最近新購買',
                '沉睡_低價值', '流失_中價值', '沉睡_高價值',
                '流失_高價值', '待喚回_低價值', '沉睡_中價值',
                '待喚回_中價值'
            ]
        }
        
        self.reset_query()
        
    def create_main_query(self, col=None):
        """Create query from sub queries."""
        if col:
            return f"""
                SELECT {','.join(col)}
                FROM ({self.sub_query['summary']})
                """
        else:
            return f"""
                SELECT *
                FROM ({self.sub_query['summary']})
                """
        
    def reset_query(self, col=None):
        """Reset all queries to default."""
        # reset sub queries
        self.sub_query = {
            'summary': f"""
                SELECT {','.join(self.col_names['summary'])}
                FROM {self.database_id}.summary
                """,
            'member': None,
            'order': None,
        }
        # reset main queries
        self.main_query = self.create_main_query()
        
        # reset clause
        self.sql_clause = {}

    def get_bq_data(self, callback=None):
        """
        Fetch data from BigQuery using the main query and return a pandas DataFrame.

        :param preprocess_function: Optional function to preprocess the data
        """
        client = Client()
        df = pd.read_gbq(query=self.main_query, dialect='standard')
        
        if callback:
            df = callback(df)
        
        return df
    
    def print_query(self):
        """Print the main query with indentation."""
        formatted_query = textwrap.indent(self.main_query.strip(), '\t')
        print(formatted_query)

    def update_query(self, col=None):
        """Add clause into sub query."""
        flag = False
        # add clause to sub queries
        for table, clause in self.sql_clause.items():
            if table in self.sub_query:
                if self.sub_query[table]:
                    self.sub_query[table] = self.sub_query[table] + '\n' + clause
                else:
                    self.sub_query[table] = clause
            elif table == 'main':
                flag = True
                main_clause = clause
            else:
                print(f"Table '{table}' not found")
        
        self.main_query = self.create_main_query(col)
        
        # add clause to main query
        if flag:
            self.main_query = self.main_query + '\n' + main_clause

if __name__ == '__main__':
    bq = BigQueryLoader()
    
    bq.sql_clause['summary'] = "WHERE rfm_new in ('活躍_高價值')\nAND last_login <= 5"
    bq.update_query(bq.col_names['main_indicator'])
    bq.print_query()
    indicators = bq.get_bq_data(lambda df: {col:df[col].item() for col in df.columns})
    print(indicators)
    
    bq.reset_query()
    bq.sql_clause['summary'] = "WHERE rfm_new in ('活躍_高價值')\nAND last_login <= 5"
    bq.sql_clause['main'] = "LIMIT 30"
    bq.update_query()
    bq.print_query()
    df = bq.get_bq_data()
    print(df.head())