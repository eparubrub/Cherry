__author__ = 'Emmit'
import time
from UserPackage import *
from Driver import *
from Timer import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from itertools import zip_longest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class Supreme:
    def __init__(self):
        self.supreme_start_page = "http://www.supremenewyork.com/shop/all/accessories"
        self.supreme_checkout = 'http://www.supremenewyork.com/checkout'
        self.autofill_url = "https://chrome.google.com/webstore/detail/autofill/nlmmgnhgdeffjkdckmikfpnddkbbfkkk?hl=en"
        self.profile = UserProfile()
        self.selection = UserSelection()
        self.settings = UserSettings()

    def setup(self):
        bot = Driver(self.settings.driver_path, self.settings.user, self.settings.headless, self.settings.delay)

        bot.go_to(self.autofill_url)

        bot.stall()

    def checkout(self):
        timer = Timer('08:00:00.010000')

        # timer.wait_until_start_time()

        timer.start()

        bot = Driver(self.settings.driver_path, self.settings.user, self.settings.headless, self.settings.delay)

        bot.go_to(self.supreme_start_page)

        bot.select_style(self.selection.style, self.selection.keywords, self.supreme_start_page)

        bot.delay()

        # bot.select_size()

        bot.add_to_cart()

        bot.delay()

        bot.go_to(self.supreme_checkout)

        bot.check_page_checkout(self.supreme_checkout)

        bot.check_autofill()

        bot.process_payment()

        timer.end()

        timer.print_time()


def main():
    supreme = Supreme()

    # supreme.setup()

    supreme.checkout()


if __name__ == "__main__":
    main()


