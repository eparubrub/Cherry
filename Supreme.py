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
        self.driver_settings = DriverSettings()
        self.profile = UserProfile()
        self.selection = UserSelection()
        self.user_settings = UserSettings()

    def setup(self):
        bot = Driver(self.user_settings.driver_path, self.user_settings.user, self.user_settings.headless, self.user_settings.delay)

        bot.go_to(self.driver_settings.autofill_url)

        bot.stall()

    def checkout_with_profile(self):
        timer = Timer(self.driver_settings.autofill_url)

        # timer.wait_until_start_time()


        bot = Driver(self.user_settings.driver_path, self.user_settings.user, self.user_settings.headless, self.user_settings.delay)

        # bot.go_to("https://www.google.com")
        #
        # bot.delay()
        # bot.delay()
        # bot.delay()
        # bot.delay()

        timer.start()

        bot.go_to(self.driver_settings.supreme_start_page)

        bot.select_style(self.selection.style, self.selection.keywords, self.driver_settings.supreme_start_page)

        bot.delay()

        # bot.select_size()

        bot.add_to_cart()

        bot.delay()

        bot.go_to(self.driver_settings.supreme_checkout)

        bot.check_page_checkout()

        bot.check_autofill()

        bot.process_payment()

        timer.end()

        timer.print_time()

    def checkout_no_profile(self):
        timer = Timer(self.driver_settings.autofill_url)

        # timer.wait_until_start_time()

        bot = Driver(self.user_settings.driver_path, None, self.user_settings.headless, self.user_settings.delay)

        timer.start()

        bot.go_to(self.driver_settings.supreme_start_page)

        bot.select_style(self.selection.style, self.selection.keywords, self.driver_settings.supreme_start_page)

        bot.delay()

        # bot.select_size()

        bot.add_to_cart()

        bot.delay()

        bot.go_to(self.driver_settings.supreme_checkout)

        bot.check_page_checkout()

        bot.manual_autofill(
            profile_name=self.user_settings.name,
            profile_email=self.user_settings.email,
            profile_tel=self.user_settings.tel,
            profile_address=self.user_settings.address,
            profile_apt=self.user_settings.apt,
            profile_zip=self.user_settings.zip,
            profile_city=self.user_settings.city,
            profile_card=self.user_settings.card,
            profile_month=self.user_settings.month,
            profile_year=self.user_settings.year,
            profile_cvv=self.user_settings.cvv,
            safe_autofill=self.user_settings.safe_autofill
        )

        bot.process_payment()

        timer.end()

        timer.print_time()


def main():
    supreme = Supreme()

    # supreme.setup()

    supreme.checkout()


if __name__ == "__main__":
    main()


