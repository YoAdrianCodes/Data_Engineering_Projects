import pandas as pd 
import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime
import sqlite3

file_path = 'Countries_by_GDP.csv'
log_file = 'etl_project_log.txt'
table_name = 'Countries_by_GDP'
db = 'World_Economies.db'
table_attributes = ['Country', 'GDP_USD_millions']
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
sql_connection = sqlite3.connect(db)
sql_query = f"SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100;"
# Code for ETL operations on Country-GDP data

# Importing the required libraries
def extract(url, table_attribs):
    df = pd.DataFrame(columns=table_attribs)
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    print(rows)
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {
                    "Country": col[0].a.contents[0],
                    "GDP_USD_millions": col[2].contents[0]
                }
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df

def transform(df):
    GDP_list = df["GDP_USD_millions"].tolist()
    GDP_list = [float("".join(x.split(','))) for x in GDP_list]
    GDP_list = [np.round(x/1000, 2) for x in GDP_list]
    df['GDP_USD_millions'] = GDP_list
    df = df.rename(columns= {"GDP_USD_millions":"GDP_USD_billions"})
    return df

def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    

def run_query(query_statement, sql_connection):
    sql_output = pd.read_sql(query_statement, sql_connection)
    print(query_statement)
    print(sql_output)

def log_progress(message):
    time_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(time_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

log_progress("ETL Job")
log_progress("Extract phase begins")
extracted_data = extract(url, table_attributes)
log_progress("Extract phase ended")

log_progress("Transform phase begins")
trans_data = transform(extracted_data)
log_progress("Transform phase ended")

log_progress("Load phase begins")
load_to_csv(trans_data, file_path)
log_progress("Load phase ended")

log_progress("Load to db phase begins")
load_to_db(trans_data, sql_connection, table_name)
log_progress("Load to db phase ended")

log_progress("Query db phase begins")
run_query(sql_query, sql_connection)
log_progress("Query db phase ended")

log_progress("ETL Job completed")
sql_connection.close()