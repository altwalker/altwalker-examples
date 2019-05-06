using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using NUnit.Framework;

using System;
using ecommerce.snipcart.jekyll.example.dotnet.pages;

namespace ecommerce.snipcart.jekyll.example.dotnet
{
    public class CheckoutModel
    {
        public IWebDriver driver;

        Home HomePage;
        Base BasePage;

        public void setUpModel()
        {
            driver = TestContext.driver;
            HomePage = new Home(TestContext.driver);
            BasePage = HomePage;
        }

        public void billing_address()
        {
            Assert.IsTrue(BasePage.is_billing_cart_view());
        }

        public void cart_open_and_not_empty()
        {
            Assert.IsTrue(BasePage.is_cart_open());
            Assert.IsTrue(BasePage.items_in_cart());
            Assert.IsTrue(BasePage.is_content_cart_view());
        }

        public void fill_billing_and_go_to_payment()
        {
            BasePage.fill_in_billing_adress_form("Altwalker", "Cluj-Napoca", "hello@test.test", "42012", "42 Cloud Street");
            BasePage.click_billing_address_next();
        }

        public void fill_payment_and_go_to_confirmation()
        {
            BasePage.click_payment_next_step_button();
        }

        public void go_to_billing_address()
        {
            BasePage.click_content_cart_next_step_button();
        }

        public void go_to_homepage()
        {
            HomePage.close_cart_button();
            HomePage.click_home_button();
        }

        public void homepage()
        {
            BasePage.wait_for_snipcart();
            Assert.IsTrue(HomePage.is_products_list_present());
        }

        public void order_confirmation()
        {
            Assert.IsTrue(BasePage.is_order_confirmation_cart_view());
        }

        public void order_confirmed()
        {
            Assert.IsTrue(BasePage.is_order_placed());
        }

        public void payment_method()
        {
            Assert.IsTrue(BasePage.is_payment_cart_view());
        }

        public void place_order()
        {
            BasePage.click_order_confirmation_place_order_button();
        }

    }
}
