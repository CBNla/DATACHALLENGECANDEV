# import libraries
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd

quote_page = 'https://www.nspower.ca/clean-energy/todays-energy-stats'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
#name_box = soup.find("div", attrs={"class": "c-card__body js-bars", "id": "pp-bars"}).find("span", attrs={"class": "stat-number"})
#name_box = soup.find_all("div", attrs={"class": "c-stat-bar__bar"}) ##.find_previous("h2", attrs={"class": "stat-text"})
date_box = soup.find("span", attrs={"class": "ppcl-date"})
date_box = date_box.get_text()
#print(date_box)
name_box = soup.find("strong").find_next("h2")
name_box = name_box.get_text()
name_box = name_box.strip("MW")
name_box2 = soup.find("strong").find_next("strong")
#.find_parent("p", attrs={"class": "c-stat-bar__disclaimer tiny align-center"})
name_box2 = name_box2.get_text()
name_box2 = name_box2.strip("MW available capacity")
table = []
table.append(name_box)
table.append(name_box2)


df1=pd.DataFrame(columns=['Time','Demand','Supply'])
df1=df1.append({'Time' : date_box,'Demand':table[0],'Supply':table[1]}, ignore_index=True)
    
df1.to_csv('novaScotia.csv',index=False,encoding='cp1252')