import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self, driver_path, user, headless):
        options = Options()

        if headless:
            options.add_argument("--headless")

        options.add_argument(user)

        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)

    def safe_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

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
                    search_keyword = self.driver.find_elements_by_link_text("//*[contains(text(), '" + keywords + "')]")
                    self.safe_click(search_keyword)
            else:
                search_keyword = self.driver.find_elements_by_link_text("//*[contains(text(), '" + keywords + "')]")
                self.safe_click(search_keyword)

        # TODO: Implement a red screen to show user to click on a style
        except Exception as e:
            print("exception: ", e)

            while self.driver.current_url == start_url:
                time.sleep(.01)

    def add_to_cart(self):
        self.driver.find_element_by_xpath("//input[@name='commit'][@type='submit']").click()

    def delay(self, time_to_delay):
        time.sleep(time_to_delay)

    def check_page_checkout(self, checkout_url):
        while self.driver.current_url != checkout_url:
            time.sleep(.01)

    def process_payment(self):
        self.driver.find_element_by_xpath("//input[@name='commit' and @type='submit']").click()
