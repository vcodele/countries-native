# List of countries and dependencies and their capitals in native languages

import requests as rs
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"

page = rs.get(url)

soup = bs(page.content, 'html.parser')

tables = soup.find_all('table', attrs={'class':'wikitable'})

#print(len(tables))

all_rows = []
headings = []

table1 = tables[1]
table1_section = table1.find_all('tr')

head = table1_section[0]

# to print the data columns
for item in head.find_all('th'):
    cln = (item.text).rstrip('\n')
    headings.append(cln)

# to iterate over all tables data
for temp in range(len(tables)):
    table1 = tables[temp]

    sections = table1.find_all('tr')

    body = sections[1:]

# iterate over the datasets of each tables
    for row_num in range(len(body)):
        row = []

# clean the datasets of each tables
        for row_item in body[row_num].find_all('td'):
            clean = re.sub("(\xa0)|(\n)|,","",row_item.text)
            row.append(clean)
        all_rows.append(row)

df = pd.DataFrame(data=all_rows, columns=headings)
df.to_csv('dataset.csv')