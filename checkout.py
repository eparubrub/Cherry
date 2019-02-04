__author__ = 'Emmit'
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from itertools import zip_longest
from selenium.webdriver.support.ui import Select
from datetime import datetime

time_now = datetime.now().strftime("%H:%M:%S.%f")

start_url = "http://www.supremenewyork.com/shop/all/accessories"


#Enter information below
keywords = ''
style = ''

name = ''
email = ''
tel = ''
address = ''
apt = ''
zip = ''
city = ''
card = ''
month = ''
year = ''
cvv = ''

safe_autofill = True
headless_tf = False
pre_start = False
delay = .55

chrome_options = Options()
chrome_options.add_argument("--headless")

if pre_start == True:
    time_now = datetime.now().strftime("%H:%M:%S.%f")
    time_start = '08:00:00.010000'
    while time_now < time_start:
        time.sleep(.01)
        time_now = datetime.now().strftime("%H:%M:%S.%f")


print('RELEASED')
print("Current time: " + time_now)

#time test
time_start = time.time()

# if headless_tf == True:
#     browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)
# else:
#     browser = webdriver.Chrome()

#enter a chrome driver below
chromedriver = "/Users/Emmit/Desktop/parubobot/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get(start_url)

try:
    if style != '':
        search_link = browser.find_elements_by_link_text(keywords)
        backup = browser.find_element_by_link_text(keywords)
        search_link2 = browser.find_elements_by_link_text(style)
        found_style = False;

        for link in search_link:
            for link2 in search_link2:
                if link.get_attribute('href') == link2.get_attribute('href'):
                    link.click()
                    found_style = True;

        if found_style == False:
            backup.click()
    else:
        search_link = browser.find_elements_by_link_text(keywords)
        search_link.click()
except:
    while browser.current_url == start_url:
        time.sleep(.01)

time.sleep(delay)

add_to_cart = browser.find_element_by_xpath("//input[@name='commit'][@type='submit']")
add_to_cart.click()

time.sleep(delay)

browser.get('http://www.supremenewyork.com/checkout')

while browser.current_url != 'http://www.supremenewyork.com/checkout':
    time.sleep(.01)

name_box = browser.find_element_by_id('order_billing_name')
email_box = browser.find_element_by_id('order_email')
tel_box = browser.find_element_by_id('order_tel')
address_box = browser.find_element_by_id('bo')
apt_box = browser.find_element_by_id('oba3')
zip_box = browser.find_element_by_id('order_billing_zip')
city_box = browser.find_element_by_id('order_billing_city')
card_box = browser.find_element_by_id('nnaerb')
cvv_box = browser.find_element_by_id('orcer')

select_month = Select(browser.find_element_by_id('credit_card_month'))
select_year = Select(browser.find_element_by_id('credit_card_year'))

if (safe_autofill == True ):
    for n, e, t, ad, ap, z, ci, ca, cv in zip_longest(name, email, tel, address, apt, zip, city, card, cvv,  fillvalue=None):
        if (n != None):
            name_box.send_keys(n)
        if (e != None):
            email_box.send_keys(e)
        if (t != None):
            tel_box.send_keys(t)
        if (ad != None):
            address_box.send_keys(ad)
        if (ap != None):
            apt_box.send_keys(ap)
        if (z != None):
            zip_box.send_keys(z)
        if (ci != None):
            city_box.send_keys(ci)
        if (ca != None):
            card_box.send_keys(ca)
        if (cv != None):
            cvv_box.send_keys(cv)
else:
    for i in name:
        name_box.send_keys(i)
    for i in email:
        email_box.send_keys(i)
    for i in tel:
        tel_box.send_keys(i)
    for i in address:
        address_box.send_keys(i)
    for i in apt:
        apt_box.send_keys(i)
    for i in zip:
        zip_box.send_keys(i)
    for i in city:
        city_box.send_keys(i)
    for i in card:
        card_box.send_keys(i)
    for i in cvv:
        cvv_box.send_keys(i)


select_month.select_by_visible_text(month)
select_year.select_by_visible_text(year)

terms = browser.find_element_by_xpath("//input[@name='order[terms]'][@type='checkbox']")
hover = ActionChains(browser).move_to_element(terms)
hover.click().perform()

process_payment = browser.find_element_by_xpath("//input[@name='commit'][@type='submit']")
#process_payment.click()
time_final = time.time()

print('ran in ' + str(round(time_final-time_start, 3)) + ' seconds')

#for screen shotting
    #browser.get_screenshot_as_file("capture.png")
    #browser.quit()

