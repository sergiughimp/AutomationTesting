import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        pass

    # @unittest.skipIf(environment == "PRODUCTION", "Do not run on production")
    def test_nothing(self):
        assert 1 + 1 == 2

    @unittest.skip
    def test_something(self):
        assert len("Michael") == 7

    def tearDown(self):
        pass

class JulesTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://jules.app/sign-in")
        self.driver.maximize_window()

    def test_forgot_password(self):
        forgot_password = self.driver.find_element(By.XPATH, '//a[@data-test-id="forgot-password-link"]')
        forgot_password.click()
        # assert self.driver.current_url == "https://jules.app/forgot-password"
        expected_url = "https://jules.app/forgot-password"
        self.assertEqual(self.driver.current_url, expected_url, "URL don't match")
        self.assertIn("forgot-password", self.driver.current_url)

    def tearDown(self):
        self.driver.close()
