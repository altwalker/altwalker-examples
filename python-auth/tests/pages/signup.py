from selenium.webdriver.common.by import By

from .base import Base


class SignUpPage(Base):
    """ Interact with element on the create account page """

    username_field = (By.ID, "id_username")
    email_field = (By.ID, "id_email")
    password_field = (By.ID, "id_password1")
    password_confirm_field = (By.ID, "id_password2")
    sign_up_btn = (By.CSS_SELECTOR, ".signup")

    sign_up_static_txt = (By.CSS_SELECTOR, ".text-center h2")

    def get_page_header_text(self):
        return self.find_element(*self.sign_up_static_txt).get_attribute("innerHTML")

    # fill in functions

    def fill_username(self, username):
        self.find_element(*self.username_field).send_keys(username)

    def fill_email(self, email):
        self.find_element(*self.email_field).send_keys(email)

    def fill_password(self, password):
        self.find_element(*self.password_field).send_keys(password)

    def confirm_password(self, password):
        self.find_element(*self.password_confirm_field).send_keys(password)

    # click functions

    def click_sign_up(self):
        self.find_element(*self.sign_up_btn).click()
