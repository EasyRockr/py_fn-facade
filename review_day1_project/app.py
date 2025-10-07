from controller.fx_controller import Fx

try:
    print("Fx App")
    print("[1] View Available Rates")
    Fx("json").display_rates()
except Exception as ex:
    print(f"Error in starting application: {str(ex)}")
