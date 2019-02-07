from random import randint

from selenium.webdriver.common.by import By

from .base import BasePage


class ProductPage(BasePage):
    """ Interact with elements commnon on Home page """
    product_details_selector = (By.CSS_SELECTOR, ".product-details")
    add_to_cart_button_selector = (By.CSS_SELECTOR, ".product-details button.snipcart-add-item")

    # check functions

    def is_product_page(self):
        self.is_element_present(*self.product_details_selector)

    # action functions

    def add_to_cart_click(self):
        product = self.find_element(*self.add_to_cart_button_selector)
        product.click()
