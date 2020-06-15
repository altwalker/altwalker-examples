import random
import string

from pypom import Page
from selenium.webdriver.common.by import By


class Base(Page):
    """ Interact with elements commnon on every page """

    URL_TEMPLATE = '/{locale}'
    DEFAULT_WAIT = 20

    home_btn = (By.CSS_SELECTOR, ".btn-outline-primary")

    def __init__(self, selenium, base_url, locale="", **url_kwargs):
        super(Base, self).__init__(
            selenium, base_url, locale=locale, **url_kwargs)

    def random_string(self, stringLength=5):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    def get_random_email(self):
        return self.random_string() + "." + self.random_string() + str(random.randint(1000, 10000)) + "@testemail.com"

    def get_random_username(self):
        return self.random_string() + "." + self.random_string()

    def get_random_password(self):
        return self.random_string() + str(random.randint(1000, 10000))

    # click functions

    def click_home_btn(self):
        self.find_element(*self.home_btn).click()
