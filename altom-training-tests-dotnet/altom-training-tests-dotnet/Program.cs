using Altom.AltWalker;
namespace altom.training.tests.dotnet.Tests {
	public class Program {
		public static void Main (string[] args) {
			ExecutorService service = new ExecutorService();
			service.RegisterModel<RegisterModel>();
			service.Run(args);
		}
	}
}
