from pypom import Page

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class snipcart_initialized():
    """An expectation for checking if snipcart is initialized"""

    def __call__(self, driver):
        return driver.execute_script("return Snipcart._initialized && Snipcart.ready;")


class BasePage(Page):
    """ Interact with elements commnon on every page """
    cart_button_locator = (By.CSS_SELECTOR, "header .snipcart-checkout")
    cart_locator = (By.ID, "snip-layout-cart-content")
    cart_close_button_locator = (By.ID, "snipcart-close")
    home_button_locator = (By.CSS_SELECTOR, "header .site-title")

    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        return super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    def is_cart_button_present(self):
        return self.is_element_present(*self.cart_button_locator)

    def is_cart_open(self):
        return self.is_element_present(*self.cart_locator)

    def items_in_cart(self):
        return int(
            self.find_element(*self.cart_button_locator).find_element(By.CSS_SELECTOR, ".snipcart-total-items").text)

    def click_cart_button(self):
        WebDriverWait(self.driver, 10).until(snipcart_initialized())
        self.find_element(*self.cart_button_locator).click()

    def click_close_cart_button(self):
        self.find_element(*self.cart_close_button_locator).click()

    def click_home_button(self):
        self.find_element(*self.home_button_locator).click()

    def wait_for_cart_reload(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#snipcart-sub-content"))
        )
