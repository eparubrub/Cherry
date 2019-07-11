__author__ = 'Emmit'
import requests
from bs4 import BeautifulSoup
import time

#enter url below
url = ""
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

while True:
    page2 = requests.get(url)
    soup2 = BeautifulSoup(page.content, 'html.parser')
    if soup != soup2:
        while True:
            print("UPDATED")
        soup = soup2
    else:
        time.sleep(5)
        continue
