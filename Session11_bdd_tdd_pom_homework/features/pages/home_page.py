from selenium.webdriver.common.by import By
class HomePage:

    URL = "https://the-internet.herokuapp.com/"
    FORM_AUTHENTICATION_SELECTOR = (By.XPATH, '//a[@href="/login"]')
    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def click_form_authentication_button(self):
        login_button = self.driver.find_element(*self.FORM_AUTHENTICATION_SELECTOR)
        login_button.click()