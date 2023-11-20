from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class InventoryPage():

    URL = 'https://www.saucedemo.com/inventory.html'
    TITLE_SELECTOR = (By.CLASS_NAME, 'title')
    PRODUCTS_SELECTOR = (By.CLASS_NAME, 'inventory_item')
    ADD_TO_CART_SELECTOR = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    REMOVE_FROM_CART_SELECTOR = (By.ID, 'remove-sauce-labs-bike-light')
    CART_BADGE_SELECTOR = (By.CLASS_NAME, 'shopping_cart_badge')
    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        title_element = self.driver.find_element(*self.TITLE_SELECTOR)
        return title_element.text

    def get_products_count(self):
        products = self.driver.find_elements(*self.PRODUCTS_SELECTOR)
        return len(products)

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_SELECTOR)
        add_to_cart_button.click()

    def remove_product_from_cart_exists(self):
        try:
            self.driver.find_element(*self.REMOVE_FROM_CART_SELECTOR)
            return True
        except NoSuchElementException:
            return False
        return True

    def get_cart_badge_counter(self):
       cart_badge_counter = self.driver.find_element(*self.CART_BADGE_SELECTOR)
       return cart_badge_counter.text