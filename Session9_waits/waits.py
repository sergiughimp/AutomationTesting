import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.hackerrank.com/")
driver.maximize_window()
time.sleep(2)


# explicit wait = used when the element is not available yet
# WebDriverWait(driver, 10) = object of type WebDriverWait that waits maxim 10 seconds
# EC.presence_of_element_located((By.XPATH, '//img[@class="custom-logo"]'))
    # EC = expected condition
    # presence_of_element_located = contion of wait

# logo_selector = driver.find_element(By.XPATH, '//img[@class="custom-logo"]')
logo_selector = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//img[@class="custom-logo"]'))
)


# contact_us_button = driver.find_element(By.LINK_TEXT, "Contact us")

contact_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Contact us"))
)
contact_button.click()

time.sleep(2)


driver.implicitly_wait(10) # start from here the code will wait 10 seconds for each element

driver.close()