using Altom.AltWalker;

using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using NUnit.Framework;

using System;

namespace ecommerce.snipcart.jekyll.example.dotnet
{

    public class Program
    {

        public static void Main(string[] args)
        {
            ExecutorService service = new ExecutorService();
            service.RegisterModel<NavigationModel>();
            service.RegisterModel<CheckoutModel>();
            service.RegisterSetup<Setup>();
            service.Run(args);
        }
    }

    public class TestContext
    {
        public static IWebDriver driver;
    }

    public class Setup
    {
        public void setUpRun()
        {
            FirefoxOptions options = new FirefoxOptions();
            options.AddArguments("--headless");
            TestContext.driver = new FirefoxDriver(options);
            TestContext.driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);
        }

        public void tearDownRun()
        {
            TestContext.driver.Quit();
        }
    }
}
