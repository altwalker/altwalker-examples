from random import randint

from selenium.webdriver.common.by import By

from .base import BasePage


class HomePage(BasePage):
    """Interact with elements on the home page."""

    _products_locator = (By.CSS_SELECTOR, ".products div.product")
    _add_to_cart_button_locator = (By.CSS_SELECTOR, "button.snipcart-add-item")

    @property
    def is_products_list_present(self):
        return self.is_element_present(*self._products_locator)

    @property
    def products_cout(self):
        return len(self.find_elements(*self._products_locator))

    def click_random_product(self):
        product_index = randint(0, self.products_cout - 1)
        return self.click_product(product_index)

    def click_product(self, product_index):
        product = self.find_elements(*self._products_locator)[product_index]
        product.find_element(By.CSS_SELECTOR, "a.product").click()

    def add_to_cart_random_product(self):
        product_index = randint(0, self.products_cout - 1)
        return self.add_to_cart_product(product_index)

    def add_to_cart_product(self, product_index):
        product = self.find_elements(*self._products_locator)[product_index]
        product.find_element(*self._add_to_cart_button_locator).click()
