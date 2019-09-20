__author__ = 'Emmit'
import time
from UserPackage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from itertools import zip_longest
from selenium.webdriver.support.ui import Select
from datetime import datetime

time_now = datetime.now().strftime("%H:%M:%S.%f")
start_url = "http://www.supremenewyork.com/shop/all/accessories"

profile = UserProfile()
selection = UserSelection()
settings = UserSettings()

if settings.pre_start == True:
    time_now = datetime.now().strftime("%H:%M:%S.%f")
    time_start = '08:00:00.010000'
    while time_now < time_start:
        time.sleep(.01)
        time_now = datetime.now().strftime("%H:%M:%S.%f")
    print('RELEASED')
    print("Current time: " + time_now)


#time test
time_start = time.time()

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# if settings_headless == True:
#     browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)
# else:
#     browser = webdriver.Chrome()



#enter a chrome driver below
chromedriver = "helper_utilities/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(executable_path=chromedriver)
# chrome_options = Options()
# chrome_options.add_argument("--headless")
browser.get(start_url)

# try:
#     if selection.style != '':
#         search_link = browser.find_elements_by_link_text(selection.keywords)
#         backup = browser.find_element_by_link_text(selection.keywords)
#         search_link2 = browser.find_elements_by_link_text(selection.style)
#         found_style = False;
#
#         for link in search_link:
#             for link2 in search_link2:
#                 if link.get_attribute('href') == link2.get_attribute('href'):
#                     link.click()
#                     found_style = True;
#
#         if found_style == False:
#             backup.click()
#     else:
#         search_link = browser.find_elements_by_link_text(selection.keywords)
#         search_link.click()
# except:
#     while browser.current_url == start_url:
#         time.sleep(.01)

browser.find_element_by_xpath("//*[contains(text(), 'Tagless')]").click()

time.sleep(settings.delay)

add_to_cart = browser.find_element_by_xpath("//input[@name='commit'][@type='submit']")
add_to_cart.click()

time.sleep(settings.delay)

browser.get('http://www.supremenewyork.com/checkout')

# while browser.current_url != 'http://www.supremenewyork.com/checkout':
#     time.sleep(.01)

name_box = browser.find_element_by_xpath("//*[text()='name']//following-sibling::input")
email_box = browser.find_element_by_xpath("//*[text()='email']//following-sibling::input")
tel_box = browser.find_element_by_xpath("//*[text()='tel']//following-sibling::input")
address_box = browser.find_element_by_xpath("//*[text()='address']//following-sibling::input")
apt_box = browser.find_element_by_xpath("//*[contains(text(),'apt')]//following-sibling::input")
zip_box = browser.find_element_by_xpath("//*[text()='zip']//following-sibling::input")
city_box = browser.find_element_by_xpath("//*[text()='city']//following-sibling::input")
card_box = browser.find_element_by_xpath("//*[text()='number']//following-sibling::input")
cvv_box = browser.find_element_by_xpath("//*[text()='CVV']//following-sibling::input")
select_month = Select(browser.find_element_by_id('credit_card_month'))
select_year = Select(browser.find_element_by_id('credit_card_year'))

if settings.safe_autofill:
    for n, e, t, ad, ap, z, ci, ca, cv in zip_longest(profile.name, profile.email, profile.tel,
                                                      profile.address, profile.apt, profile.zip,
                                                      profile.city, profile.card, profile.cvv, fillvalue=None):
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
    for i in profile.name:
        name_box.send_keys(i)
    for i in profile.email:
        email_box.send_keys(i)
    for i in profile.tel:
        tel_box.send_keys(i)
    for i in profile.address:
        address_box.send_keys(i)
    for i in profile.apt:
        apt_box.send_keys(i)
    for i in profile.zip:
        zip_box.send_keys(i)
    for i in profile.city:
        city_box.send_keys(i)
    for i in profile.card:
        card_box.send_keys(i)
    for i in profile.cvv:
        cvv_box.send_keys(i)


select_month.select_by_visible_text(profile.month)
select_year.select_by_visible_text(profile.year)

terms = browser.find_element_by_xpath("//input[@id='order_terms']")
hover = ActionChains(browser).move_to_element(terms)
hover.click().perform()

# process_payment = browser.find_element_by_xpath("//input[@name='commit' and @type='submit']")
# process_payment.click()

time_final = time.time()

print('ran in ' + str(round(time_final-time_start, 3)) + ' seconds')

#for screen shotting
#browser.get_screenshot_as_file("capture.png")
#browser.quit()