import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_25'
csv_path = './top_25_films.csv'
df = pd.DataFrame(columns=["Film","Year", "Rotten Tomatoes' Top 100"])
count = 0

# load web page as HTML document
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# from this point each run is different
# I believe it might be because the webpage 
# is not loading completely (maybe it needs
# to be allowed more time to load?)
# my VPN or browser may be affecting it (is that a thing?)

# find all tables
tables = data.find_all('tbody')

# get rows from first table
rows = tables[0].find_all('tr')

for row in rows:
    if count < 25:
        col = row.find_all('td')
        if len(col)!=0:
            
            data_dict = {"Film": col[1].contents[0],
                         "Year": int(col[2].contents[0]),
                         "Rotten Tomatoes' Top 100": col[3].contents[0]}

            df1 = pd.DataFrame(data_dict, index=[0])
            
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

# filter for movies released in the 2000 (2000 included)
filtered_df = df[df["Year"] >= 2000]
filtered_df.to_csv(csv_path)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()