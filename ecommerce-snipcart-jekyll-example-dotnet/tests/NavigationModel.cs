using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using NUnit.Framework;

using System;
using ecommerce.snipcart.jekyll.example.dotnet.pages;

namespace ecommerce.snipcart.jekyll.example.dotnet
{
    public class NavigationModel
    {

        Home HomePage;
        Base BasePage;
        Product ProductPage;
        public IWebDriver driver;

        public void setUpModel()
        {
            driver = TestContext.driver;
            HomePage = new Home(TestContext.driver);
            ProductPage = new Product(TestContext.driver);
            BasePage = HomePage;
        }

        public void add_to_cart_from_homepage()
        {
            HomePage.add_to_cart_product();
        }

        public void add_to_cart_from_product_page()
        {
            ProductPage.add_to_cart_product();
        }

        public void cart_open_and_not_empty()
        {
            Assert.IsTrue(BasePage.is_cart_open());
            Assert.IsTrue(BasePage.items_in_cart());
            Assert.IsTrue(BasePage.is_content_cart_view());
        }

        public void close_cart()
        {
            HomePage.close_cart_button();
        }

        public void do_nothing()
        {
        }

        public void go_to_homepage()
        {
            BasePage.click_home_button();
        }

        public void go_to_product_page()
        {
            HomePage.click_product();
        }

        public void homepage()
        {
            BasePage.wait_for_snipcart();
            Assert.IsTrue(HomePage.is_products_list_present());
        }

        public void homepage_cart_open()
        {
            Assert.IsTrue(BasePage.is_cart_open());
        }

        public void load_home_page()
        {
            driver.Navigate().GoToUrl("https://altom.gitlab.io/altwalker/snipcart-jekyll-ecommerce-demo/");
            driver.Manage().Window.Maximize();
            System.Threading.Thread.Sleep(5000);
        }

        public void open_cart()
        {
            BasePage.click_cart_button();
        }

        public void product_page()
        {
            BasePage.wait_for_snipcart();
            Assert.IsTrue(ProductPage.is_products_list_present());
        }

        public void product_page_cart_open()
        {
            Assert.IsTrue(BasePage.is_cart_open());
        }

    }
}
