from selenium import webdriver
from selenium.webdriver.common.by import By

from .base import Base


class ChangePwdPage(Base):
    """ Interact with element on the change password page """

    old_pwd_field = (By.ID, "id_old_password")
    new_pwd1_field = (By.ID, "id_new_password1")
    new_pwd2_field = (By.ID, "id_new_password2")
    change_pwd_btn = (By.CSS_SELECTOR, ".change-pwd")

    return_home_btn = (By.CSS_SELECTOR, ".text-center p a")
    password_changed_text = (By.CSS_SELECTOR, ".text-center p")

    change_password_static_txt = (By.CSS_SELECTOR, ".text-center h2")

    def get_page_header_text(self):
        return self.find_element(*self.change_password_static_txt).get_attribute("innerHTML")

    def get_password_changed_text(self):
        return self.find_element(*self.password_changed_text).get_attribute("innerHTML")

    # fill in functions

    def fill_old_pwd(self, old_pwd):
        self.find_element(*self.old_pwd_field).send_keys(old_pwd)

    def fill_new_pwd(self, new_pwd):
        self.find_element(*self.new_pwd1_field).send_keys(new_pwd)

    def confirm_pwd(self, new_pwd):
        self.find_element(*self.new_pwd2_field).send_keys(new_pwd)

    # click functions

    def click_change_btn(self):
        self.find_element(*self.change_pwd_btn).click()

    def click_home_btn(self):
        self.find_element(*self.return_home_btn).click()
