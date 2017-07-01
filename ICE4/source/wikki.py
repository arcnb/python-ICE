import requests
from bs4 import BeautifulSoup
import os

url = "https://en.wikipedia.org/wiki/Google"

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
result_list1 = soup.findAll('div')
for div in result_list1:
    X=div.find('h1')
    if (X!=None):
        print(X)
        print('\n')

body = soup.find('div', {'class': 'mw-parser-output'})
print(body.text)
