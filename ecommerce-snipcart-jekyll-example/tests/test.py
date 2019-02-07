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
    driver.implicitly_wait(30)
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

    def edge_loadHomePage(self):
        print("Load the Ecommerce home page")
        home_page = HomePage(self.driver, "https://dorinoltean.github.io/snipcart-jekyll-integration/")
        home_page.open()

    def edge_addToCartFromHomePage(self):
        home_page = HomePage(self.driver)
        home_page.add_to_cart_random_product()

    def edge_navigateToProductPage(self):
        home_page = HomePage(self.driver)
        home_page.click_random_product()

    def edge_closeCart(self):
        page = BasePage(self.driver)
        page.click_close_cart_button()

    def edge_goToHomePage(self):
        page = BasePage(self.driver)
        page.click_home_button()

    def edge_addToCartFromProductPage(self):
        page = ProductPage(self.driver)
        page.add_to_cart_click()

    # vertices

    def vertex_homepage(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_products_list_present())

    def vertex_productPage(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_product_page())

    def vertex_homepageCartOpen(self):
        page = BasePage(self.driver)
        self.assertTrue(page.is_cart_open())

    def vertex_pageCartOpen(self):
        page = BasePage(self.driver)
        self.assertTrue(page.is_cart_open())


# if __name__ == "__main__":
# 	setUpRun()
# 	model = NavigationModel()
# 	model.setUpModel()
# 	model.edge_loadHomePage()
# 	model.edge_addProductToCartFromHomePage()
# 	tearDownRun()
