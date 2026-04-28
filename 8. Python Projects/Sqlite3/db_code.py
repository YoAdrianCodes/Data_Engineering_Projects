import sqlite3
import pandas as pd

#connect and create a new db
conn = sqlite3.connect('STAFF.db')

#create the table name and attributes
table_name = 'INSTRUCTORS'  
attributes_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = 'INSTRUCTOR.csv'
#create the dataframe from the csv file
df = pd.read_csv(file_path, names=attributes_list)

#create the table in the database
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('table is ready')

#Run basic sql queries to check the data

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# append new data to the table in the db
data_dict = {
    'ID': [100],
    'FNAME': ['John'],
    'LNAME': ['Doe'],
    'CITY': ['Pairs'],
    'CCODE': ['FR']
}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('data appended successfully')
conn.close()