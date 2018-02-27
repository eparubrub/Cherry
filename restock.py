__author__ = 'Emmit'
import requests
import urllib3
from bs4 import BeautifulSoup
import webbrowser
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('')

while True:
    url = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #edit accordingly
    name_box = soup.find('b', attrs={'class': 'button sold-out'})
    string_button = str(name_box)
    string_none = "None"
    if string_button == string_none:
        print('UPDATED')
        webbrowser.open(url)
        break
    else:
        time.sleep(60)
        continue
