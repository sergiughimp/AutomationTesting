'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
    - setUp()
        - Driver
        https://the-internet.herokuapp.com/
        Click pe Form Authentication
    tearDown()
        Quit browser
'''
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):
    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()
        form_authentication = self.driver.find_element(By.XPATH, '//a[@href="/login"]')
        form_authentication.click()

    def tearDown(self):
        self.driver.close()

    # ● Test 1
    #   - Verifică dacă noul url e corect
    def test_check_url(self): # test 1
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(self.driver.current_url, expected_url, "URL doesn't match")

    # ● Test 2
    #     - Verifică dacă page title e corect
    def test_title(self): # test 2
        title_page = self.driver.find_element(By.CSS_SELECTOR, "h2").text
        print(title_page)
        self.assertEqual(title_page, "Login Page", "Title doesn't match")
    # ● Test 3
    #     - Verifică textul de pe elementul xpath=//h2 e corect
    def test_h2_right(self): # test 3
        h2_title = self.driver.find_element(By.XPATH, '//h2').text
        self.assertEqual(h2_title, "Login Page", "Title doesn't match")
    # ● Test 4
    #     - Verifică dacă butonul de login este displayed
    def test_login_button_displayed(self): # test 4
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        self.assertTrue(login_button, "Login button is not displayed")
    # ● Test 5
    #     - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_href_attribute(self): # test 5
        href_attribute = self.driver.find_element(By.XPATH, '//a[@href="http://elementalselenium.com/"]').text
        self.assertEqual(href_attribute, "Elemental Selenium", "Href attribute doesn't match")
    # ● Test 6
    #     - Lasă goale user și pass
    #     - Click login
    #     - Verifică dacă eroarea e displayed
    def test_error_displayed(self): # test 6
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()
        error = self.driver.find_element(By.ID, "flash")
        self.assertTrue(error, "Error message is not displayed")

    # ● Test 7
    #     - Completează cu user și pass invalide
    #     - Click login
    #     - Verifică dacă mesajul de pe eroare e corect
    #     - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    #     expected = 'Your username is invalid!'
    #     self.assertTrue(expected in actual, 'Error message text is incorrect')
    def test_error_message(self): # test 7
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys("tomsmith43")
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("NoPassword")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()

        expected_error_message = 'Your username is invalid!'
        self.assertTrue(expected_error_message, 'Error message text is incorrect')

    # ● Test 8
    #     - Lasă goale user și pass
    #     - Click login
    #     - Apasă x la eroare
    #     - Verifică dacă eroarea a dispărut
    def test_error_disappear(self): # test 8
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()

        close_error_button = self.driver.find_element(By.CLASS_NAME, 'close')
        close_error_button.click()

        try:
            # Wait for the error_message to become invisible
            error_message = WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.ID, "flash"))
            )
            print(f"Error message {error_message} is now invisible.")
        except Exception as e:
            print(f"Error: {e}")
    # ● Test 9
    #     - Ia ca o listă toate //label
    #     - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
    #     - Aici e ok să avem 2 asserturi
    def test_text_label(self): # test 9
        labels = self.driver.find_elements(By.CSS_SELECTOR, "label")
        self.assertEqual(labels[0].text, "Username", "Text from first label is wrong")
        self.assertEqual(labels[1].text, "Password", "Text from second label is wrong")

    # ● Test 10
    #     - Completează cu user și pass valide
    #     - Click login
    #     - Verifică ca noul url CONTINE /secure
    #     - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    #     - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    #     - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    def test_secure_text(self): # test 10
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys("tomsmith")
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("SuperSecretPassword!")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()

        expected_url = "https://the-internet.herokuapp.com/secure"
        self.assertEqual(self.driver.current_url, expected_url, "URL doesn't contains secure")

        try:
            # Wait for the success_message to be visible
            success_message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "flash"))
            )
            print(f"Success message {success_message.text} is displayed.)
            self.assertIn("secure area!", success_message.text,"Required text is not int the message.")
        except Exception as e:
            print(f"Error: {e}")

    # ● Test 11
    #     - Completează cu user și pass valide
    #     - Click login
    #     - Click logout
    #     - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    def test_login_logout(self): # test 11
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys("tomsmith")
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("SuperSecretPassword!")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button')
        login_button.click()

        logout_button = self.driver.find_element(By.XPATH, '//a[@href="/logout"]')
        logout_button.click()

        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(self.driver.current_url, expected_url, "URL doesn't match")
