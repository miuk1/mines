import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from path import grid



# url = 'https://pg-0451682683.fs-playground.com/'
url = 'http://localhost:3226'
driver = webdriver.Firefox('firefoxdriver')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

table_row_data = soup.find_all('tr')

data = []
for row in table_row_data:
    cols = row.find_all('td')
    cols_class = [ele['class'][0] for ele in cols]
    data.append(cols_class)

mines = {
    'full': 1,
    'empty': 0,
    'start': 1,
    'end': 1
}

data_grid = []

for i in data:
    data_grid.append([mines[x] for x in i])

print(grid(data_grid))


# moves = {
#     "L": "Left",
#     "R": "Right",
#     "U": "Up",
#     "D": "Down"
# }
