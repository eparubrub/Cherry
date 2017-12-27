__author__ = 'Emmit'
import requests
import urllib3
from bs4 import BeautifulSoup
import webbrowser
import time
import smtplib

while True:
    url = "http://www.supremenewyork.com/shop/accessories/geobpzkvf"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name_box = soup.find('b', attrs={'class': 'button sold-out'})
    string1 = str(name_box)
    Nonerino = "None"
    if string1 == Nonerino:
        print('ITS UPDATED U GOON')
        print(string1)
        webbrowser.open(url)
        break
    else:
        time.sleep(60)
        continue