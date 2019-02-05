import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.home import HomePage

driver = None

def setUpRun():
	global driver
	options = Options()
	#options.add_argument('-headless')

	print("Create a new Firefox session")
	driver = webdriver.Firefox(options=options)

	print("Implicity wait and maximize the window")
	driver.implicitly_wait(20)
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
		self.home_page = HomePage(self.driver, "https://dorinoltean.github.io/snipcart-jekyll-integration/")
		self.home_page.open()


if __name__ == "__main__":
	setUpRun()
	model = NavigationModel()
	model.setUpModel()
	model.edge_loadHomePage()
	tearDownRun()