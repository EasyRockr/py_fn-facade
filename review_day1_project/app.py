from controller.fx_controller import Fx

def main():
    while True:
        print("Fx App")
        print("[1] View Available Rates")
        print("[2] Convert Money")
        option = input("option: ").strip()

        fx = Fx("json")

        if option == "1":
            fx.display_rates()
        elif option == "2":
            fx.convert_money()
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()
