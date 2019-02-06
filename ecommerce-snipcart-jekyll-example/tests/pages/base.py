from pypom import Page

from selenium.webdriver.common.by import By


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

    def click_cart_button(self):
        self.find_element(*self.cart_button_locator).click()

    def click_close_cart_button(self):
        self.find_element(*self.cart_close_button_locator).click()

    def click_home_button(self):
        self.find_element(*self.home_button_locator).click()
