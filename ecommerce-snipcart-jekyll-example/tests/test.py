import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from tests.pages.base import BasePage
from tests.pages.home import HomePage
from tests.pages.product import ProductPage

driver = None


def setUpRun():
    global driver
    options = Options()
    # options.add_a	rgument('-headless')

    print("Create a	 new Firefox session")
    driver = webdriver.Firefox(options=options)

    print("Implicity wait and maximize the window")
    driver.implicitly_wait(15)
    driver.maximize_window()


def tearDownRun():
    global driver

    print("Close the Firefox session")
    driver.quit()


class NavigationModel(unittest.TestCase):
    def setUpModel(self):
        global driver

        print("Set up for Navigation model")
        self.driver = driver

    def load_home_page(self):
        print("Load the Ecommerce home page")
        home_page = HomePage(self.driver, "https://dorinaltom.gitlab.io/snipcart-jekyll-ecommerce-demo/")
        home_page.open()

    def add_to_cart_from_homepage(self):
        page = HomePage(self.driver)
        page.add_to_cart_random_product()
        page.wait_for_cart_reload()

    def go_to_product_page(self):
        home_page = HomePage(self.driver)
        home_page.click_random_product()

    def close_cart(self):
        page = BasePage(self.driver)
        page.click_close_cart_button()

    def go_to_homepage(self):
        page = BasePage(self.driver)
        page.click_home_button()

    def add_to_cart_from_product_page(self):
        page = ProductPage(self.driver)
        page.add_to_cart_click()
        page.wait_for_cart_reload()

    def open_cart(self):
        page = BasePage(self.driver)
        page.click_cart_button()

    def do_nothing(self):
        pass

    # vertices

    def homepage(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_products_list_present())

    def product_page(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_product_page())

    def homepage_cart_open(self):
        page = BasePage(self.driver)
        self.assertTrue(page.is_cart_open())

    def product_page_cart_open(self):
        page = BasePage(self.driver)
        self.assertTrue(page.is_cart_open())

    def cart_open_and_not_empty(self):
        page = BasePage(self.driver)
        self.assertTrue(page.is_cart_open())
        self.assertTrue(page.items_in_cart() > 0)


class CheckoutModel(unittest.TestCase):
    def setUpModel(self):
        global driver

        print("Set up for Navigation model")
        self.driver = driver

    # edges - actions

    def finish_checkout(self):
        page = BasePage(self.driver)
        page.click_close_cart_button()
        page.click_home_button()

    # vertices - states

    def cart_open_and_not_empty(self):
        page = BasePage(self.driver)
        self.assertTrue(page.is_cart_open())
        self.assertTrue(page.items_in_cart() > 0)

    def homepage(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_products_list_present())


# if __name__ == "__main__":
# 	setUpRun()
# 	model = NavigationModel()
# 	model.setUpModel()
# 	model.edge_loadHomePage()
# 	model.edge_addProductToCartFromHomePage()
# 	tearDownRun()
