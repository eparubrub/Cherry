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

        bot.go_to("https://www.google.com")

        bot.delay()
        bot.delay()
        bot.delay()
        bot.delay()

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

        bot.checkout_page_scan()

        bot.manual_autofill(
            profile_name=self.profile.name,
            profile_email=self.profile.email,
            profile_tel=self.profile.tel,
            profile_address=self.profile.address,
            profile_apt=self.profile.apt,
            profile_zip=self.profile.zip,
            profile_city=self.profile.city,
            profile_card=self.profile.card,
            profile_month=self.profile.month,
            profile_year=self.profile.year,
            profile_cvv=self.profile.cvv,
            safe_autofill=self.profile.safe_autofill
        )

        # bot.process_payment()

        timer.end()

        timer.print_time()


def main():
    supreme = Supreme()

    # supreme.setup()

    supreme.checkout_no_profile()
    
    # supreme.checkout_with_profile()


if __name__ == "__main__":
    main()


