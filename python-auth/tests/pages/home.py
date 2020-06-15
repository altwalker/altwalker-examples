from selenium.webdriver.common.by import By

from .base import Base


class HomePage(Base):
    """ Interact with element on the main page """

    login_btn = (By.CSS_SELECTOR, ".login")
    logout_btn = (By.CSS_SELECTOR, ".logout")
    change_pwd_btn = (By.CSS_SELECTOR, ".change-pwd")

    # click functions

    def click_login(self):
        self.find_element(*self.login_btn).click()

    def click_logout(self):
        self.find_element(*self.logout_btn).click()

    def click_change_pwd(self):
        self.find_element(*self.change_pwd_btn).click()
