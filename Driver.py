import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from itertools import zip_longest


class Driver:
    def __init__(self, driver_path, user, headless, delay):
        options = Options()

        if headless:
            options.add_argument("--headless")

        options.add_argument(user)

        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)

        self.delay_time = delay

        # Product page xpaths
        self.submit_xpath = "//input[@name='commit'][@type='submit']"

        # Checkout page xpaths
        self.process_payment_xpath = "//input[@name='commit' and @type='submit']"
        self.name_field_xpath = "//*[text()='name']//following-sibling::input"
        self.email_field_xpath = "//*[text()='email']//following-sibling::input"
        self.tel_field_xpath = "//*[text()='tel']//following-sibling::input"
        self.address_field_xpath = "//*[text()='address']//following-sibling::input"
        self.apt_field_xpath = "//*[contains(text(),'apt')]//following-sibling::input"
        self.zip_field_xpath = "//*[text()='zip']//following-sibling::input"
        self.city_field_xpath = "//*[text()='city']//following-sibling::input"
        self.card_field_xpath = "//*[text()='number']//following-sibling::input"
        self.cvv_field_xpath = "//*[text()='CVV']//following-sibling::input"
        self.select_month_xpath = "//*[@id='credit_card_month']"
        self.select_year_xpath = "//*[@id='credit_card_year']"
        self.terms_xpath = "//input[@id='order_terms']"

        # Element initializer
        self.submit_element = None
        self.process_payment_element = None
        self.name_field_element = None
        self.email_field_element = None
        self.tel_field_element = None
        self.address_field_element = None
        self.apt_field_element = None
        self.zip_field_element = None
        self.city_field_element = None
        self.card_field_element = None
        self.cvv_field_element = None
        self.select_month_element = None
        self.select_year_element = None

    def safe_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def delay(self):
        time.sleep(self.delay_time)

    def stall(self):
        while self.driver.current_url != "":
            time.sleep(1)

    def go_to(self, url):
        self.driver.get(url)

    def grab_screenshot(self):
        self.driver.get_screenshot_as_file("screenshot.png")
        self.driver.quit()

    def select_style(self, style, keywords, start_url):
        try:
            if style != '':
                search_style_keywords = self.driver.find_elements_by_xpath("//a[contains(text(), '" + style + "')]//ancestor::article//a[contains(text(), '" + keywords + "')]")
                if len(search_style_keywords) > 0:
                    self.safe_click(search_style_keywords[0])
                else:
                    self.safe_click("//*[contains(text(), '" + keywords + "')]")
            else:
                self.safe_click(self.driver.find_element_by_xpath("//*[contains(text(), '" + keywords + "')]"))

        # TODO: Implement a red screen to show user to click on a style
        except Exception as e:
            print("exception: ", e)

            while self.driver.current_url == start_url:
                time.sleep(.01)

    def add_to_cart(self):
        self.driver.find_element_by_xpath(self.submit_xpath).click()

    def check_page_checkout(self, checkout_url):

        while self.driver.current_url != checkout_url:
            print("expecting checkout url but current url stuck at:", self.driver.current_url)
            time.sleep(.01)

    def process_payment(self):
        self.driver.find_element_by_xpath(self.process_payment_xpath).click()

    def checkout_page_scan(self):
        self.name_field_element = self.driver.find_element_by_xpath(self.name_field_xpath)
        self.email_field_element = self.driver.find_element_by_xpath(self.email_field_xpath)
        self.tel_field_element = self.driver.find_element_by_xpath(self.tel_field_xpath)
        self.address_field_element = self.driver.find_element_by_xpath(self.address_field_xpath)
        self.apt_field_element = self.driver.find_element_by_xpath(self.apt_field_xpath)
        self.zip_field_element = self.driver.find_element_by_xpath(self.zip_field_xpath)
        self.city_field_element = self.driver.find_element_by_xpath(self.city_field_xpath)
        self.card_field_element = self.driver.find_element_by_xpath(self.card_field_xpath)
        self.cvv_field_element = self.driver.find_element_by_xpath(self.cvv_field_xpath)
        self.select_month_element = Select(self.driver.find_element_by_xpath(self.select_month_xpath))
        self.select_year_element = Select(self.driver.find_element_by_xpath(self.select_year_xpath))
        self.process_payment_element = self.driver.find_element_by_xpath(self.process_payment_xpath)

    def check_autofill(self):
        if self.name_field_element.get_attribute("aria_invalid"):
            print("No autofill provided, resorting to manual autofill")

    def manual_autofill(self, **kwargs):
        profile_name = kwargs.get('profile_name')
        profile_email = kwargs.get('profile_email')
        profile_tel = kwargs.get('profile_tel')
        profile_address = kwargs.get('profile_address')
        profile_apt = kwargs.get('profile_apt')
        profile_zip = kwargs.get('profile_zip')
        profile_city = kwargs.get('profile_city')
        profile_card = kwargs.get('profile_card')
        profile_cvv = kwargs.get('profile_cvv')
        profile_month = kwargs.get('profile_month')
        profile_year = kwargs.get('profile_year')

        safe_autofill = kwargs.get('safe_autofill')

        if safe_autofill:
            for name, email, telephone, address, apartment, zipcode, city, card, cvv in zip_longest(
                                                          profile_name, profile_email, profile_tel,
                                                          profile_address, profile_apt, profile_zip,
                                                          profile_city, profile_card, profile_cvv, fillvalue=None):
                if name is not None:
                    self.name_field_element.send_keys(name)
                if email is not None:
                    self.email_field_element.send_keys(email)
                if telephone is not None:
                    self.tel_field_element.send_keys(telephone)
                if address is not None:
                    self.address_field_element.send_keys(address)
                if apartment is not None:
                    self.apt_field_element.send_keys(apartment)
                if zipcode is not None:
                    self.zip_field_element.send_keys(zipcode)
                if city is not None:
                    self.city_field_element.send_keys(city)
                if card is not None:
                    self.card_field_element.send_keys(card)
                if cvv is not None:
                    self.cvv_field_element.send_keys(cvv)
        else:
            for name in profile_name:
                self.name_field_element.send_keys(name)
            for email in profile_email:
                self.email_field_element.send_keys(email)
            for telephone in profile_tel:
                self.tel_field_element.send_keys(telephone)
            for address in profile_address:
                self.address_field_element.send_keys(address)
            for apartment in profile_apt:
                self.apt_field_element.send_keys(apartment)
            for zipcode in profile_zip:
                self.zip_field_element.send_keys(zipcode)
            for city in profile_city:
                self.city_field_element.send_keys(city)
            for card in profile_card:
                self.card_field_element.send_keys(card)
            for cvv in profile_cvv:
                self.cvv_field_element.send_keys(cvv)

        self.select_month.select_by_visible_text(profile_month)
        self.select_year.select_by_visible_text(profile_year)

        terms = self.driver.find_element_by_xpath(self.terms_xpath)
        hover = ActionChains(self.driver).move_to_element(terms)
        hover.click().perform()
