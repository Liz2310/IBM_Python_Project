import sqlite3
import pandas as pd

database_name = "./Movies.db"
table_name = "Top_25"
column_name = "Film, Year"
condition = "Year == 2019"

sql_connection = sqlite3.connect(database_name)


sql_query1 = f"SELECT * FROM {table_name}"
df1 = pd.read_sql(sql_query1, sql_connection)
print(df1)
print()


sql_query2 = f"SELECT COUNT(*) FROM {table_name}"
df2 = pd.read_sql(sql_query2, sql_connection)
print(df2)
print()

sql_query3 = f"SELECT {column_name} FROM {table_name}"
df3 = pd.read_sql(sql_query3, sql_connection)
print(df3)
print()

sql_query4 = f"SELECT * FROM {table_name} WHERE {condition}"
df4 = pd.read_sql(sql_query4, sql_connection)
print(df4)
print()