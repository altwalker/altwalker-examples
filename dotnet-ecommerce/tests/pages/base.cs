using OpenQA.Selenium;

using System;
using ExpectedConditions = SeleniumExtras.WaitHelpers.ExpectedConditions;
using OpenQA.Selenium.Support.UI;

namespace dotnet.ecommerce.pages
{
    public class Base
    {
        private const string closeCartBtn = "snipcart-close";
        private const string accessCartBtn = "header .snipcart-checkout";
        private const string goHomeHeader = "header .site-title";
        private const string nextStepOnCartContent = "#snipcart-main-content #snipcart-actions a";
        private const string billingName = "snip-name";
        private const string billingCity = "snip-city";
        private const string billingEmail = "snip-email";
        private const string billingAddress = "snip-address1";
        private const string billingPostalCode = "snip-postalCode";
        private const string nextStepBillingBtn = "snipcart-next";
        private const string nextPaymentMethodBtn = "snipcart-paymentmethod-pay";
        private const string placeOrderBtn = "a.js-submit";
        private const string cartLocator = "snipcart-main-content";
        private const string totalPaidSection = ".snip-static__title";
        private const string itemsInCartValue = ".snip-quantity-trigger__text";

        protected readonly IWebDriver driver;

        public Base(IWebDriver driver)
        {
            this.driver = driver;
        }

        // for Navigation Model
        public void click_cart_button()
        {
            wait_for_element_is_visible(By.CssSelector(accessCartBtn)).Click();
        }

        public void close_cart_button()
        {
            wait_for_element_is_visible(By.Id(closeCartBtn)).Click();
        }

        public void click_home_button()
        {
            wait_for_element_is_visible(By.CssSelector(goHomeHeader)).Click();
        }

        // for Checkout Model
        public void click_content_cart_next_step_button()
        {
            IWebElement theNextStepOnCartContent = wait_for_element_is_visible(By.CssSelector(nextStepOnCartContent));
            theNextStepOnCartContent.Click();
        }

        public void fill_in_billing_adress_form(string name, string city, string email, string street_address1, string postal_code)
        {

            driver.FindElement(By.Id(billingName)).Clear();
            driver.FindElement(By.Id(billingName)).SendKeys(name);

            driver.FindElement(By.Id(billingCity)).Clear();
            driver.FindElement(By.Id(billingCity)).SendKeys(city);

            driver.FindElement(By.Id(billingEmail)).Clear();
            driver.FindElement(By.Id(billingEmail)).SendKeys(email);

            driver.FindElement(By.Id(billingAddress)).Clear();
            driver.FindElement(By.Id(billingAddress)).SendKeys(street_address1);

            driver.FindElement(By.Id(billingPostalCode)).Clear();
            driver.FindElement(By.Id(billingPostalCode)).SendKeys(postal_code);
        }

        public void click_billing_address_next()
        {
            wait_for_element_is_visible(By.Id(nextStepBillingBtn)).Click();
        }

        public void click_payment_next_step_button()
        {
            wait_for_element_is_visible(By.Id(nextPaymentMethodBtn)).Click();
        }

        public void click_order_confirmation_place_order_button()
        {
            wait_for_element_is_visible(By.CssSelector(placeOrderBtn)).Click();
        }

        // for asserts
        public Boolean is_cart_open()
        {
            return wait_for_element_is_visible(By.Id(cartLocator)).Displayed;
        }

        public Boolean items_in_cart()
        {
            string itemsInCart = wait_for_element_is_visible(By.CssSelector(itemsInCartValue)).GetAttribute("innerHTML");
            int itemsInCartInt = Convert.ToInt32(itemsInCart);
            if (itemsInCartInt == 0)
                return false;
            return true;
        }

        public Boolean is_content_cart_view()
        {
            return wait_for_element_is_visible(By.CssSelector(nextStepOnCartContent)).Displayed;
        }

        public Boolean is_billing_cart_view()
        {
            return wait_for_element_is_visible(By.Id(nextStepBillingBtn)).Displayed;
        }

        public Boolean is_order_confirmation_cart_view()
        {
            return wait_for_element_is_visible(By.CssSelector(placeOrderBtn)).Displayed;
        }

        public Boolean is_order_placed()
        {
            return wait_for_element_is_visible(By.CssSelector(totalPaidSection)).Displayed;
        }

        public Boolean is_payment_cart_view()
        {
            return wait_for_element_is_visible(By.Id(nextPaymentMethodBtn)).Displayed;
        }

        public IWebElement wait_for_element_is_visible(By by)
        {
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
            wait.Until(ExpectedConditions.ElementIsVisible(by));
            return driver.FindElement(by);
        }

        public void wait_for_snipcart()
        {
            const string snipcartInitializedQuery = "return typeof Snipcart !== 'undefined' && typeof Snipcart._initialized !== 'undefined' && typeof Snipcart.ready !== 'undefined' && Snipcart._initialized && Snipcart.ready;";
            IJavaScriptExecutor js = (IJavaScriptExecutor) driver;

            while ((Boolean?)js.ExecuteScript(snipcartInitializedQuery) != true)
            {
                System.Threading.Thread.Sleep(500);
            }
        }
    }
}
