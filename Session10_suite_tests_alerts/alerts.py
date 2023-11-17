import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AlertsTests(unittest.TestCase):

    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    BUTTON_SELECTORS = {
        "ALERT": (By.XPATH, "//ul//li[1]/button"), # //button[@onclick='jsAlert()'] ,
        "CONFIRM": (By.XPATH, "//ul//li[2]/button"), # //button[@onclick='jsConfirm()']
        "PROMPT": (By.XPATH, "//ul//li[3]/button") # //button[@onclick='jsPrompt()']
    }
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_alert(self):
        self.driver.get(self.URL)
        alert_button = self.driver.find_element(*self.BUTTON_SELECTORS["ALERT"])
        alert_button.click()
        time.sleep(3)

        # can't interact with window alert, it is not from DOM (webpage with elements). is part from the browser
        alert = self.driver.switch_to.alert
        alert.accept() # ok button
        # alert.dismiss() # cancel button

        time.sleep(3)
        result_alert = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result_alert, "You successfully clicked an alert", "Alert wasn't with success")

    def test_prompt(self):
        self.driver.get(self.URL)
        prompt_button = self.driver.find_element(*self.BUTTON_SELECTORS["PROMPT"])
        prompt_button.click()
        time.sleep(3)

        prompt = self.driver.switch_to.alert
        prompt.send_keys("Very good!")
        time.sleep(5)
        prompt.accept()

        result_prompt = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result_prompt, "You entered: Very good!", "Prompt message is wrong!")

    def test_basic_auth(self):
        # syntax to login with basic authentication (pop-up from browser)
        url_no_auth = "https://the-internet.herokuapp.com/basic_auth"
        self.driver.get(url_no_auth)
        time.sleep(3)

        url_with_auth = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url_with_auth)
        time.sleep(3)