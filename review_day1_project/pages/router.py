from pages.page_rates import PageRates
from pages.page_convert import ConvertMenu
from pages.page_main_menu import MainMenu

class Router:
    def route_choice(self, choice):
        while True:
            try:
                choice = int(choice)
                if choice in [1, 2]:
                    break
                else:
                    print("Invalid option. Please choose 1 or 2.")
                    choice = MainMenu().display()
            except ValueError:
                print("Invalid input. Please enter a number.")
                choice = MainMenu().display()
        
        if choice == 1:
            PageRates().display_rates()
            MainMenu().display()
        elif choice == 2:
            convert_page = ConvertMenu()
            source_currency, target_currency, amount = convert_page.input_menu()
            print(f"Converting {amount} from {source_currency} to {target_currency}...")

        
