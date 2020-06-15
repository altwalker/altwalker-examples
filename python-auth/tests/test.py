import unittest
import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .pages.home import HomePage
from .pages.login import LoginPage
from .pages.signup import SignUpPage
from .pages.reset import ResetPage
from .pages.change_pwd import ChangePwdPage

import requests

driver = None
host = os.environ.get("APP_HOST", "127.0.0.1")
port = os.environ.get("APP_PORT", 8000)
BASE_URL = "http://{}:{}/".format(host, port)


def setUpRun():
    global driver
    options = Options()
    options.add_argument('-headless')

    print("Create a new Firefox session")
    driver = webdriver.Firefox(options=options)

    print("Implicitly wait and maximize the window")
    driver.implicitly_wait(20)
    driver.maximize_window()


def tearDownRun():
    global driver
    print("Saving screenshot for test run")
    fileName = time.strftime("%Y%m%d-%H%M%S")
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")
    driver.save_screenshot("screenshots/Results_%s.png" % fileName)
    print("Close the Firefox session")
    driver.quit()


class Authentication(unittest.TestCase):

    def setUpModel(self):
        global driver

        print("Set up for Navigation model")
        self.driver = driver
        self.home_page = HomePage(self.driver, BASE_URL)
        self.login_page = LoginPage(self.driver, BASE_URL)
        self.sign_up_page = SignUpPage(self.driver, BASE_URL)
        self.reset_page = ResetPage(self.driver, BASE_URL)
        self.change_pwd_page = ChangePwdPage(self.driver, BASE_URL)

    def tearDownModel(self):
        print("Tear down for Navigation model")

    # VERTICES (methods for asserts)

    def home(self):
        self.assertEqual(self.driver.current_url, BASE_URL,
                         "The home page is not the one displayed.")

    def change_password_form(self):
        self.assertEqual(self.change_pwd_page.get_page_header_text(), "Change password",
                         "The Change Password page is not the one displayed.")

    def create_account_form(self):
        # verify that the create account page is displayed
        self.assertEqual(self.change_pwd_page.get_page_header_text(
        ), "Sign up", "The Sign Up page is not the one displayed.")

    def login_form(self):
        # verify that login page is displayed
        self.assertEqual(self.login_page.get_page_header_text(
        ), "Login", "The Login page is not the one displayed.")

    def reset_password_form(self):
        # verify that we're on the reset password page
        self.assertEqual(self.reset_page.get_password_reset_header_text(
        ), "Forgot your password?", "The forgot password is not the one displayed.")

    def reset_password_success(self):
        # verify that we're on the pasword reset successful page
        self.assertEqual(self.reset_page.get_password_reset_header_text(
        ), "Password reset complete", "The success message is missing.")

    def password_changed_successfuly(self):
        self.assertEqual(self.change_pwd_page.get_password_changed_text(
        ), "Your password was changed.", "The success message is missing.")

    def account_created(self):
        self.assertEqual(self.login_page.get_page_header_text(
        ), "Login", "The Login page is not the one displayed.")

    # EDGES (methods for actions)

    def start_app(self):
        print("Load the Django Auth home page")
        self.home_page = HomePage(self.driver, BASE_URL)
        self.home_page.open()

        time.sleep(1)

        print("Implicitly wait")
        self.driver.implicitly_wait(30)

    def go_to_login(self):
        # access the login page
        self.home_page.click_login()

    def change_password(self):
        # filling all fields required to change the password successfully
        self.change_pwd_page.fill_old_pwd(self.new_password)
        self.new_password = self.change_pwd_page.get_random_password()
        self.change_pwd_page.fill_new_pwd(self.new_password)
        self.change_pwd_page.confirm_pwd(self.new_password)

        # clicking the change button
        self.change_pwd_page.click_change_btn()

    def create_account(self):
        # filling all fields required to create an account
        self.sign_up_page.fill_username(self.new_username)
        self.sign_up_page.fill_email(self.new_email)
        self.sign_up_page.fill_password(self.new_password)
        self.sign_up_page.confirm_password(self.new_password)

        # clicking the sign up button
        self.sign_up_page.click_sign_up()

    def go_back_home(self):
        # return to home page after changing password
        self.change_pwd_page.click_home_btn()

    def go_to_change_pasword(self):
        # access the change password form
        self.home_page.click_change_pwd()

    def go_to_create_account(self):
        # access the create account form
        self.login_page.click_create_account()

        self.new_username = self.sign_up_page.get_random_username()
        self.new_email = self.sign_up_page.get_random_email()
        self.new_password = self.sign_up_page.get_random_password()

    def go_back_to_login(self):
        # return to login form after resetting pasword
        self.reset_page.click_return_home()

    def go_home(self):
        # click the home button
        self.login_page.click_home_btn()

    def go_to_reset_password(self):
        # access the reset password form
        self.login_page.click_reset_pwd()

    def attempt_incorrect_repeat_pwd(self):
        # filling all fields required to change the password successfully
        self.change_pwd_page.fill_old_pwd(self.new_password)
        new_password = self.change_pwd_page.get_random_password()
        self.change_pwd_page.fill_new_pwd(new_password)
        new_password = self.change_pwd_page.get_random_password()
        self.change_pwd_page.confirm_pwd(new_password)

        # clicking the change button
        self.change_pwd_page.click_change_btn()

    def attempt_incorrect_login(self):
        # fill all fields required to login
        self.login_page.fill_username(self.new_username)
        new_password = self.login_page.get_random_password()
        self.login_page.fill_password(new_password)

        # click the login button
        self.login_page.click_login()

        self.login_page.clear_username()

    def login(self):
        # fill all fields required to login
        self.login_page.fill_username(self.new_username)
        self.login_page.fill_password(self.new_password)

        # click the login button
        self.login_page.click_login()

    def logout(self):
        # click the logout button
        self.home_page.click_logout()

    def reset_password(self):
        # fill reqired fields and click the reset password button
        self.reset_page.fill_email(self.new_email)
        self.reset_page.click_reset_pwd()

        self.assertEqual(self.reset_page.get_email_sent_text(),
                         "We've emailed you instructions for setting your password. " +
                         "You should receive the email shortly!",
                         "The email sent message is missing.")

        email_content = requests.get(
            BASE_URL + "testability/last-reset-pwd-email").text
        resetPwURL = email_content.replace(
            email_content.split("http")[0], '').split("\n")[0]
        self.driver.get(resetPwURL)

        self.new_password = self.reset_page.get_random_password()

        self.reset_page.fill_new_password1(self.new_password)
        self.reset_page.fill_new_password2(self.new_password)

        self.reset_page.click_change_pwd()

    def returned_to_login(self):
        pass
