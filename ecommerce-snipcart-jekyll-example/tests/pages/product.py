from random import randint

from selenium.webdriver.common.by import By

from .base import BasePage


class ProductPage(BasePage):
    """ Interact with elements commnon on Home page """
    products_selector = (By.CSS_SELECTOR, ".products div.product")

    # check functions

    def is_products_list_present(self):
        return self.is_element_present(*self.products_selector)

    def count_products(self):
        return len(self.find_elements(*self.products_selector))

    # action functions

    def click_random_product(self):
        product_index = randint(0, self.count_products()-1)
        return self.click_product(product_index)

    def click_product(self, product_index):
        product = self.find_elements(*self.products_selector)[product_index]
        product.find_element(By.CSS_SELECTOR, "a.product").click()

    def add_to_cart_random_product(self):
        product_index = randint(0, self.count_products()-1)
        return self.add_to_cart_product(product_index)

    def add_to_cart_product(self, product_index):
        product = self.find_elements(*self.products_selector)[product_index]
        product.find_element(By.CSS_SELECTOR, "button.snipcart-add-item").click()
