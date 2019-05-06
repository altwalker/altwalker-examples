using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using NUnit.Framework;

using System;

namespace ecommerce.snipcart.jekyll.example.dotnet.pages
{
    public class Home : Base
    {
        private const string firstProduct = "(//div[@class='product'])[1]";
        private const string addToCartBtn = "button.snipcart-add-item";

        public Home(IWebDriver driver) : base(driver)
        { }

        public void click_product()
        {
            wait_for_element_is_visible(By.XPath(firstProduct)).Click();
        }

        // for asserts
        public Boolean is_products_list_present()
        {
            return wait_for_element_is_visible(By.XPath(firstProduct)).Displayed;
        }

        public void add_to_cart_product()
        {
            wait_for_element_is_visible(By.CssSelector(addToCartBtn)).Click();
        }

    }
}