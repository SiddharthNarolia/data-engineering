import snowflake.connector as sfc
import pandas as pd
import os
import toml

SF_USER = os.getenv('SF_USER')
SF_PWD = os.getenv('SF_PWD')

with open('C:/Users/siddg/Github/all_things_data/data-engineering/snowflake/connection_config.toml', 'r') as configfile:
    config = toml.load(configfile)

config = config['default_connection']

conn = sfc.connect(password=SF_PWD,**config)

def read_data(conn, query:str):
    cursor = conn.cursor()
    query = query
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame()
    return df