from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class snipcart_initialized_and_ready():
    """An expectation for checking if snipcart is initialized."""

    def __call__(self, driver):
        return driver.execute_script("return typeof Snipcart !== 'undefined' && typeof Snipcart._initialized !== 'undefined' && typeof Snipcart.ready !== 'undefined' && Snipcart._initialized && Snipcart.ready;")  # noqa: E501


class BasePage(Page):
    """Interact with elements common on every page."""

    _home_button_locator = (By.CSS_SELECTOR, "header .site-title")
    _cart_button_locator = (By.CSS_SELECTOR, "header .snipcart-checkout")
    _cart_locator = (By.ID, "snipcart-main-content")
    _cart_close_button_locator = (By.ID, "snipcart-close")
    _total_items_in_cart_locator = (By.CSS_SELECTOR, ".snipcart-total-items")
    _cart_items_list_holder_locator = (By.CSS_SELECTOR, "#snipcart-sub-content")

    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    @property
    def is_cart_button_present(self):
        return self.is_element_present(*self._cart_button_locator)

    @property
    def is_cart_open(self):
        return self.is_element_present(*self._cart_locator)

    @property
    def total_items_in_cart(self):
        return int(self.find_element(*self._cart_button_locator).find_element(*self._total_items_in_cart_locator).text)

    def wait_for_snipcart(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(snipcart_initialized_and_ready())

    def wait_for_cart_reload(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self._cart_items_list_holder_locator)
        )

    def click_cart_button(self):
        self.wait_for_snipcart()
        self.find_element(*self._cart_button_locator).click()

    def click_close_cart_button(self):
        self.find_element(*self._cart_close_button_locator).click()

    def click_home_button(self):
        self.find_element(*self._home_button_locator).click()
