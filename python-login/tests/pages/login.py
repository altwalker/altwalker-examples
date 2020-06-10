from selenium import webdriver
from selenium.webdriver.common.by import By

from .base import Base


class LoginPage(Base):
    """ Interact with element on the login page """

    username_field = (By.ID, "id_username")
    password_field = (By.ID, "id_password")
    login_btn = (By.CSS_SELECTOR, ".login")
    create_account_btn = (By.CSS_SELECTOR, ".signup")
    reset_pwd_btn = (By.CSS_SELECTOR, ".reset-pwd")

    login_static_txt = (By.CSS_SELECTOR, ".text-center h2")

    def get_page_header_text(self):
        return self.find_element(*self.login_static_txt).get_attribute("innerHTML")

    def clear_username(self):
        self.find_element(*self.username_field).clear()

    # fill in functions

    def fill_username(self, username):
        self.find_element(*self.username_field).send_keys(username)

    def fill_password(self, password):
        self.find_element(*self.password_field).send_keys(password)

    # click functions

    def click_login(self):
        self.find_element(*self.login_btn).click()

    def click_create_account(self):
        self.find_element(*self.create_account_btn).click()

    def click_reset_pwd(self):
        self.find_element(*self.reset_pwd_btn).click()
