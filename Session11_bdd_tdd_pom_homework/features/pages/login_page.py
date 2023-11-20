from selenium.webdriver.common.by import By

class LoginPage:

    URL = "https://the-internet.herokuapp.com/login"
    TITLE_SELECTOR = (By.TAG_NAME, 'h2')


    USERNAME_SELECTOR = (By.ID, "username")
    PASSWORD_SELECTOR = (By.ID, "password")
    LOGIN_BUTTON_SELECTOR = (By.TAG_NAME, "button")
    # ERROR_MESSAGE_SELECTOR = (By.XPATH, '//h3[@data-test="error"]')
    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        title_element = self.driver.find_element(*self.TITLE_SELECTOR)
        return title_element.text

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()