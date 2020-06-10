from selenium import webdriver
from selenium.webdriver.common.by import By

from .base import Base


class ResetPage(Base):
    """ Interact with element on the reset password page """

    email_field = (By.ID, "id_email")
    reset_pwd_btn = (By.CSS_SELECTOR, ".reset-pwd")
    email_sent_text = (By.CSS_SELECTOR, ".text-center p")
    password_reset_password_header = (By.CSS_SELECTOR, ".text-center h1")
    new_pwd1_field = (By.ID, "id_new_password1")
    new_pwd2_field = (By.ID, "id_new_password2")
    change_my_pwd_btn = (By.CSS_SELECTOR, ".reset-pwd-confirm")
    return_home_btn = (By.CSS_SELECTOR, ".text-center p a")

    def get_email_sent_text(self):
        return self.find_element(*self.email_sent_text).get_attribute("innerHTML")

    def get_password_reset_header_text(self):
        return self.find_element(*self.password_reset_password_header).get_attribute("innerHTML")

    # fill in functions

    def fill_email(self, email):
        self.find_element(*self.email_field).send_keys(email)

    def fill_new_password1(self, password):
        self.find_element(*self.new_pwd1_field).send_keys(password)

    def fill_new_password2(self, password):
        self.find_element(*self.new_pwd2_field).send_keys(password)

    # click functions

    def click_reset_pwd(self):
        self.find_element(*self.reset_pwd_btn).click()

    def click_change_pwd(self):
        self.find_element(*self.change_my_pwd_btn).click()

    def click_return_home(self):
        self.find_element(*self.return_home_btn).click()
