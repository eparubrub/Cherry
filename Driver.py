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

    def go_to(self, url):
        self.driver.get(url)

    def grab_screenshot(self):
        self.driver.get_screenshot_as_file("screenshot.png")
        self.driver.quit()

    def select_style(self, style, keywords, start_url):
        try:
            if style != '':
                search_list_keywords = self.driver.find_elements_by_link_text(keywords)
                search_list_style = self.driver.find_elements_by_link_text(style)
                backup = self.driver.find_element_by_link_text(keywords)
                found_style = False;

                # Search for style and keyword match, if not, pick first keyword
                for keyword in search_list_keywords:
                    for style in search_list_style:
                        if keyword.get_attribute('href') == style.get_attribute('href'):
                            keyword.click()
                            found_style = True

                if not found_style:
                    backup.click()

            else:
                search_keyword = self.driver.find_elements_by_link_text(keywords)
                search_keyword.click()
        except:
            while self.driver.current_url == start_url:
                time.sleep(.01)
