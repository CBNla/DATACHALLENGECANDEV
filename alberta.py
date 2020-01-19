# importing libraries
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd


def get_table(table):
    table_content=[]
    #rows are tagged tr, columns td
    ROWS=table.find_all("tr")
    for row in ROWS:
        row_content=[]
        COLUMNS=row.find_all("td")
        for column in COLUMNS:
            row_content.append(column.get_text())
        table_content.append(row_content)
    return table_content

url = "http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet"
try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")
soup = BeautifulSoup(page, 'html.parser')

#################################################################
updated=soup.find(string=re.compile("Last Update")) #re.compile lets us search using just part of the string
print(updated)
#keep only the date and time
updated=updated.strip("Last Update :")
print(updated)
#################################################################
summary = soup.find("b").find_previous("table") #, re.compile("^SUMMARY"))
summary_table = get_table(summary)
del summary_table[0]
##################################################################
df=pd.DataFrame(columns=['Summary','Energy'])
for sublist in summary_table:
    print(sublist)
    df=df.append({'Summary':sublist[0],'Energy':sublist[1]}, ignore_index=True)
    
df.to_csv('AESO_Summary_'+updated+'.csv',index=False,encoding='cp1252')






