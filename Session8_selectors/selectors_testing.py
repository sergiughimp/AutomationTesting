import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://formy-project.herokuapp.com/form")
driver.maximize_window()
time.sleep(2)

# id - selector
# <input type="text" class="form-control" id="first-name" placeholder="Enter first name">
first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys("Michael")
last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys("Jordan")
time.sleep(2)

# link_text - selector
# <a class="navbar-brand" id="logo" href="/">Formy</a>
logo = driver.find_element(By.LINK_TEXT, "FORMY")
logo.click()
assert driver.current_url == "https://formy-project.herokuapp.com/", "Wrong URL"
time.sleep(2)

# partial_link_text - selector
# <a class="btn btn-lg" href="/form">Complete Web Form</a>
complete_form_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Complete ")
complete_form_link.click()
time.sleep(2)

# tag name - selector
# <h1>Complete Web Form</h1>
page_title = driver.find_element(By.TAG_NAME, "h1")
assert page_title.text == "Complete Web Form", "Wrong title of the page"

# tag name - selector
input_elements = driver.find_elements(By.TAG_NAME,"input")
input_elements[0].send_keys("David")
input_elements[1].send_keys("Luca")
time.sleep(2)

# class - selector
job_title_input = driver.find_elements(By.CLASS_NAME, "form-control")[2]
job_title_input.send_keys("Software Developer")
time.sleep(2)

# css selectors = can group multiple types of selectors (TAG_NAME, ID (#), CLASS (.), others (attribute_name = ["value"]))
# <h1>Complete Web Form</h1>
page_title_css_selector = driver.find_element(By.CSS_SELECTOR, "h1")
print(page_title_css_selector.text)

# css selector - :nth-child(1)
form_group = driver.find_element(By.CSS_SELECTOR, "div.form-group")
radio_button = form_group.find_element(By.CSS_SELECTOR, "div:nth-child(1) input#radio-button-1")
radio_button.click()
time.sleep(2)

# css selector - id
checkbox_male = driver.find_element(By.XPATH, '//*[@id="checkbox-1"]')
checkbox_male.click()
time.sleep(2)

# css selector - function
submit_button = driver.find_element(By.XPATH, '//a[text()="Submit"]')
submit_button.click()
time.sleep(2)

driver.close()


