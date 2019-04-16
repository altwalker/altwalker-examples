using Altom.AltWalker;
namespace ecommerce.snipcart.jekyll.example.dotnet.Tests {
	public class Program {
		public static void Main (string[] args) {
			ExecutorService service = new ExecutorService();
			service.RegisterModel<NavigationModel>();
			service.RegisterModel<CheckoutModel>();
			service.Run(args);
		}
	}
}
