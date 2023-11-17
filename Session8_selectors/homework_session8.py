'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unul sau mai multe din sugestiile de site-uri de mai jos
    - https://www.phptravels.net/
    - http://automationpractice.com/index.php
    - https://formy-project.herokuapp.com/
    - https://the-internet.herokuapp.com/
    - https://www.techlistic.com/p/selenium-practice-form.html
    - jules.app
Alege câte 1 element din fiecare tip de selector din următoarele categorii:
    ● Id
    ● Link text
    ● Parțial link text
    ● Css
    ● Xpath
'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(2)

form_authentication = driver.find_element(By.LINK_TEXT, "Form Authentication")
form_authentication.click()

# id - selector
username = driver.find_element(By.ID, 'username')
username.send_keys("tomsmith")

# xpath - selector
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("SuperSecretPassword!")

# css - selector
login_button = driver.find_element(By.CSS_SELECTOR, "#login > button")
login_button.click()

time.sleep(5)

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(2)

# partial_link_text - selector
disappear_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Disappearing ")
disappear_element.click()
time.sleep(2)

# link_text - selector
home = driver.find_element(By.LINK_TEXT, "Home")
home.click()
time.sleep(2)
driver.close()