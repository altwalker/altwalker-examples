using Altom.AltWalker;

using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

using System;

namespace dotnet.ecommerce
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Start the executor service
            ExecutorService service = new ExecutorService();

            // Register the setup class and the classes for all models
            service.RegisterSetup<Setup>();
            service.RegisterModel<NavigationModel>();
            service.RegisterModel<CheckoutModel>();

            // Start the executor service
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
