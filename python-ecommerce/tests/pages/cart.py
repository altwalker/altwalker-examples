from selenium.webdriver.common.by import By

from .base import BasePage


class CartPage(BasePage):
    """Interact with element on the cart page."""

    _content_cart_next_step_button_locator = (By.CSS_SELECTOR, "#snipcart-main-content #snipcart-actions a")
    _billing_addres_next_step_button_locator = (By.ID, "snipcart-next")
    _payment_next_step_button_locator = (By.ID, "snipcart-paymentmethod-pay")
    _order_confirmation_place_order_button_locator = (By.CSS_SELECTOR, "a.js-submit")
    _billing_address_form_locator = (By.ID, "snipcart-billingaddress-form")

    _billing_name_locator = (By.ID, "snip-name")
    _billing_city_locator = (By.ID, "snip-city")
    _billing_email_locator = (By.ID, "snip-email")
    _billing_street_address1_locator = (By.ID, "snip-address1")
    _billing_postal_code_locator = (By.ID, "snip-postalCode")

    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    @property
    def is_content_next_button_present(self):
        return self.is_element_present(*self._content_cart_next_step_button_locator)

    @property
    def is_billing_next_button_present(self):
        return self.is_element_present(*self._billing_addres_next_step_button_locator)

    @property
    def is_payment_next_button_present(self):
        return self.is_element_present(*self._payment_next_step_button_locator)

    @property
    def is_order_confirmation_present(self):
        return self.is_element_present(*self._order_confirmation_place_order_button_locator)

    def click_content_cart_next_step_button(self):
        self.wait_for_snipcart()
        self.find_element(*self._content_cart_next_step_button_locator).click()

    def click_billing_addres_next_step_button(self):
        self.wait_for_snipcart()
        self.find_element(*self._billing_addres_next_step_button_locator).click()

    def click_payment_next_step_button(self):
        self.wait_for_snipcart()
        self.find_element(*self._payment_next_step_button_locator).click()

    def click_order_confirmation_place_order_button(self):
        self.wait_for_snipcart()
        self.find_element(*self._order_confirmation_place_order_button_locator).click()

    def fill_in_billing_adress_form(self, name="", city="", email="", street_address1="", postal_code=""):
        print("Fill Billing Form")

        if name != "":
            self.find_element(*self._billing_name_locator).clear()
            self.find_element(*self._billing_name_locator).send_keys(name)
        if city != "":
            self.find_element(*self._billing_city_locator).clear()
            self.find_element(*self._billing_city_locator).send_keys(city)
        if email != "":
            self.find_element(*self._billing_email_locator).clear()
            self.find_element(*self._billing_email_locator).send_keys(email)
        if street_address1 != "":
            self.find_element(*self._billing_street_address1_locator).clear()
            self.find_element(*self._billing_street_address1_locator).send_keys(street_address1)
        if postal_code != "":
            self.find_element(*self._billing_postal_code_locator).clear()
            self.find_element(*self._billing_postal_code_locator).send_keys(postal_code)
