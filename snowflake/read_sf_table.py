import snowflake.connector as sfc
import pandas as pd
import os

SF_USER = os.getenv('SF_USER')
SF_PWD = os.getenv('SF_PWD')

conn = sfc.connect(user=SF_USER,
                   password=SF_PWD,
                   account='zj01766.us-east4.gcp',
                   warehouse='COMPUTE_WH',
                   database='SNAROLIA_DB',
                   schema='DATA',
                   role='ACCOUNTADMIN')

cursor = conn.cursor()

QUERY = 'select * from sample_generated_data;'

cursor.execute(QUERY)
data = cursor.fetchall()
df = pd.DataFrame(data)
df.to_csv('sample_generated_data.csv')