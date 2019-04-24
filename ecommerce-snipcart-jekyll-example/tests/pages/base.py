from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class snipcart_initialized_and_ready():
    """An expectation for checking if snipcart is initialized"""

    def __call__(self, driver):
        return driver.execute_script("return typeof Snipcart !== 'undefined' && Snipcart._initialized && Snipcart.ready;")


class BasePage(Page):
    """ Interact with elements commnon on every page """
    cart_button_locator = (By.CSS_SELECTOR, "header .snipcart-checkout")
    cart_locator = (By.ID, "snipcart-main-content")
    cart_close_button_locator = (By.ID, "snipcart-close")
    home_button_locator = (By.CSS_SELECTOR, "header .site-title")
    total_items_in_cart_locator = (By.CSS_SELECTOR, ".snipcart-total-items")
    cart_items_list_holder_locator = (By.CSS_SELECTOR, "#snipcart-sub-content")

    def wait_for_snipcart(self):
        WebDriverWait(self.driver, 10).until(snipcart_initialized_and_ready())

    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        return super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    def is_cart_button_present(self):
        return self.is_element_present(*self.cart_button_locator)

    def is_cart_open(self):
        return self.is_element_present(*self.cart_locator)

    def items_in_cart(self):
        return int(self.find_element(*self.cart_button_locator).find_element(*self.total_items_in_cart_locator).text)

    def click_cart_button(self):
        self.wait_for_snipcart()
        self.find_element(*self.cart_button_locator).click()

    def click_close_cart_button(self):
        self.find_element(*self.cart_close_button_locator).click()

    def click_home_button(self):
        self.find_element(*self.home_button_locator).click()

    def wait_for_cart_reload(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_items_list_holder_locator)
        )


class CartPage(BasePage):
    """interact with element on the cart page"""
    content_cart_next_step_button_locator = (By.CSS_SELECTOR, "#snipcart-main-content #snipcart-actions a")
    billing_addres_next_step_button_locator = (By.ID, "snipcart-next")
    payment_next_step_button_locator = (By.ID, "snipcart-paymentmethod-pay")
    order_confirmation_place_order_button_locator = (By.CSS_SELECTOR, "a.js-submit")
    billing_address_form_locator = (By.ID, "snipcart-billingaddress-form")

    billing_name_locator = (By.ID, "snip-name")
    billing_city_locator = (By.ID, "snip-city")
    billing_email_locator = (By.ID, "snip-email")
    billing_street_address1_locator = (By.ID, "snip-address1")
    billing_postal_code_locator = (By.ID, "snip-postalCode")

    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        return super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    def is_content_cart_view(self):
        return self.is_element_present(*self.content_cart_next_step_button_locator)

    def is_billing_cart_view(self):
        return self.is_element_present(*self.billing_addres_next_step_button_locator)

    def is_payment_cart_view(self):
        return self.is_element_present(*self.payment_next_step_button_locator)

    def is_order_confirmation_cart_view(self):
        return self.is_element_present(*self.order_confirmation_place_order_button_locator)

    def click_content_cart_next_step_button(self):
        self.wait_for_snipcart()
        self.find_element(*self.content_cart_next_step_button_locator).click()

    def click_billing_addres_next_step_button(self):
        self.wait_for_snipcart()
        self.find_element(*self.billing_addres_next_step_button_locator).click()

    def click_payment_next_step_button(self):
        self.wait_for_snipcart()
        self.find_element(*self.payment_next_step_button_locator).click()

    def click_order_confirmation_place_order_button(self):
        self.wait_for_snipcart()
        self.find_element(*self.order_confirmation_place_order_button_locator).click()

    def fill_in_billing_adress_form(self, name="", city="", email="", street_address1="", postal_code=""):
        print("Fill Billing Form")
        if (name != ""):
            self.find_element(*self.billing_name_locator).clear()
            self.find_element(*self.billing_name_locator).send_keys(name)
        if (city != ""):
            self.find_element(*self.billing_city_locator).clear()
            self.find_element(*self.billing_city_locator).send_keys(city)
        if email != "":
            self.find_element(*self.billing_email_locator).clear()
            self.find_element(*self.billing_email_locator).send_keys(email)
        if street_address1 != "":
            self.find_element(*self.billing_street_address1_locator).clear()
            self.find_element(*self.billing_street_address1_locator).send_keys(street_address1)
        if postal_code != "":
            self.find_element(*self.billing_postal_code_locator).clear()
            self.find_element(*self.billing_postal_code_locator).send_keys(postal_code)
