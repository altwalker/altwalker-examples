using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using NUnit.Framework;

using dotnet.ecommerce.pages;

namespace dotnet.ecommerce
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

        public void e_add_to_cart_from_homepage()
        {
            HomePage.add_to_cart_product();
        }

        public void e_add_to_cart_from_product_page()
        {
            ProductPage.add_to_cart_product();
        }

        public void v_cart_open_and_not_empty()
        {
            Assert.IsTrue(BasePage.is_cart_open());
            Assert.IsTrue(BasePage.items_in_cart());
            Assert.IsTrue(BasePage.is_content_cart_view());
        }

        public void e_close_cart()
        {
            HomePage.close_cart_button();
        }

        public void e_do_nothing()
        {
        }

        public void e_go_to_homepage()
        {
            BasePage.click_home_button();
        }

        public void e_go_to_product_page()
        {
            HomePage.click_product();
        }

        public void v_homepage()
        {
            BasePage.wait_for_snipcart();
            Assert.IsTrue(HomePage.is_products_list_present());
        }

        public void v_homepage_cart_open()
        {
            Assert.IsTrue(BasePage.is_cart_open());
        }

        public void e_load_home_page()
        {
            driver.Navigate().GoToUrl("https://altom.gitlab.io/altwalker/snipcart-jekyll-ecommerce-demo/");
            driver.Manage().Window.Maximize();
            System.Threading.Thread.Sleep(5000);
        }

        public void e_open_cart()
        {
            BasePage.click_cart_button();
        }

        public void v_product_page()
        {
            BasePage.wait_for_snipcart();
            Assert.IsTrue(ProductPage.is_products_list_present());
        }

        public void v_product_page_cart_open()
        {
            Assert.IsTrue(BasePage.is_cart_open());
        }

        public void e_close_cart_and_go_to_homepage()
        {
            BasePage.close_cart_button();
            BasePage.click_home_button();
        }
    }
}
