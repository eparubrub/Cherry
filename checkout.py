__author__ = 'Emmit'
import time
from UserPackage import *
from Driver import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from itertools import zip_longest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import datetime

time_now = datetime.now().strftime("%H:%M:%S.%f")
start_url = "http://www.supremenewyork.com/shop/all/accessories"

profile = UserProfile()
selection = UserSelection()
settings = UserSettings()

if settings.pre_start:
    time_now = datetime.now().strftime("%H:%M:%S.%f")
    time_start = '08:00:00.010000'
    while time_now < time_start:
        time.sleep(.01)
        time_now = datetime.now().strftime("%H:%M:%S.%f")
    print('RELEASED')
    print("Current time: " + time_now)
time_start = time.time()

bot = Driver(settings.driver_path, settings.user, settings.headless)

bot.go_to(start_url)

bot.select_style(settings.style, settings.keywords, start_url)

# browser.find_element_by_xpath("//*[contains(text(), 'Tagless')]").click()
#
# time.sleep(settings.delay)
#
# add_to_cart = browser.find_element_by_xpath("//input[@name='commit'][@type='submit']")
# add_to_cart.click()
#
# time.sleep(settings.delay)
#
# browser.get('http://www.supremenewyork.com/checkout')
#
# # while browser.current_url != 'http://www.supremenewyork.com/checkout':
# #     time.sleep(.01)
#
# # name_box = browser.find_element_by_xpath("//*[text()='name']//following-sibling::input")
# # email_box = browser.find_element_by_xpath("//*[text()='email']//following-sibling::input")
# # tel_box = browser.find_element_by_xpath("//*[text()='tel']//following-sibling::input")
# # address_box = browser.find_element_by_xpath("//*[text()='address']//following-sibling::input")
# # apt_box = browser.find_element_by_xpath("//*[contains(text(),'apt')]//following-sibling::input")
# # zip_box = browser.find_element_by_xpath("//*[text()='zip']//following-sibling::input")
# # city_box = browser.find_element_by_xpath("//*[text()='city']//following-sibling::input")
# # card_box = browser.find_element_by_xpath("//*[text()='number']//following-sibling::input")
# # cvv_box = browser.find_element_by_xpath("//*[text()='CVV']//following-sibling::input")
# # select_month = Select(browser.find_element_by_id('credit_card_month'))
# # select_year = Select(browser.find_element_by_id('credit_card_year'))
# #
# # if settings.safe_autofill:
# #     for n, e, t, ad, ap, z, ci, ca, cv in zip_longest(profile.name, profile.email, profile.tel,
# #                                                       profile.address, profile.apt, profile.zip,
# #                                                       profile.city, profile.card, profile.cvv, fillvalue=None):
# #         if n is not None:
# #             name_box.send_keys(n)
# #         if e is not None:
# #             email_box.send_keys(e)
# #         if t is not None:
# #             tel_box.send_keys(t)
# #         if ad is not None:
# #             address_box.send_keys(ad)
# #         if ap is not None:
# #             apt_box.send_keys(ap)
# #         if z is not None:
# #             zip_box.send_keys(z)
# #         if ci is not None:
# #             city_box.send_keys(ci)
# #         if ca is not None:
# #             card_box.send_keys(ca)
# #         if cv is not None:
# #             cvv_box.send_keys(cv)
# # else:
# #     for i in profile.name:
# #         name_box.send_keys(i)
# #     for i in profile.email:
# #         email_box.send_keys(i)
# #     for i in profile.tel:
# #         tel_box.send_keys(i)
# #     for i in profile.address:
# #         address_box.send_keys(i)
# #     for i in profile.apt:
# #         apt_box.send_keys(i)
# #     for i in profile.zip:
# #         zip_box.send_keys(i)
# #     for i in profile.city:
# #         city_box.send_keys(i)
# #     for i in profile.card:
# #         card_box.send_keys(i)
# #     for i in profile.cvv:
# #         cvv_box.send_keys(i)
# #
# #
# # select_month.select_by_visible_text(profile.month)
# # select_year.select_by_visible_text(profile.year)
# #
# # terms = browser.find_element_by_xpath("//input[@id='order_terms']")
# # hover = ActionChains(browser).move_to_element(terms)
# # hover.click().perform()
#
# # process_payment = browser.find_element_by_xpath("//input[@name='commit' and @type='submit']")
# # process_payment.click()
#
# time_final = time.time()
#
# print('ran in ' + str(round(time_final-time_start, 3)) + ' seconds')
#
## for screen shotting
# bot.grab_screenshot()


