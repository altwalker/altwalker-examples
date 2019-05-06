using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using NUnit.Framework;

using System;

namespace ecommerce.snipcart.jekyll.example.dotnet.pages
{
    public class Product : Base
    {
        private const string productDetailsSelector = ".product-details";
        private const string addToCartBtn = "button.snipcart-add-item";

        public Product(IWebDriver driver) : base(driver)
        { }

        public void add_to_cart_product()
        {
            wait_for_element_is_visible(By.CssSelector(addToCartBtn)).Click();
        }

        // for asserts
        public Boolean is_products_list_present()
        {
            return wait_for_element_is_visible(By.CssSelector(productDetailsSelector)).Displayed;
        }

    }
}