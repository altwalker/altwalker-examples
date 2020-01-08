from selenium.webdriver.common.by import By

from .base import BasePage


class ProductPage(BasePage):
    """Interact with elements on product page."""

    _product_details_locator = (By.CSS_SELECTOR, ".product-details")
    _product_name_locator = (By.CSS_SELECTOR, ".product-description p:first-child")
    _add_to_cart_button_locator = (By.CSS_SELECTOR, ".product-details button.snipcart-add-item")

    @property
    def is_product_present(self):
        return self.is_element_present(*self._product_details_locator)

    @property
    def product_name(self):
        return self.find_element(*self._product_name_locator).text

    def click_add_to_cart(self):
        self.find_element(*self._add_to_cart_button_locator).click()
