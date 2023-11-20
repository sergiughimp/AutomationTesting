from selenium.webdriver.common.by import By

class SecurePage:

    URL = "https://the-internet.herokuapp.com/secure"
    TITLE_SELECTOR = (By.TAG_NAME, 'h2')
    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        title_element = self.driver.find_element(*self.TITLE_SELECTOR)
        return title_element.text