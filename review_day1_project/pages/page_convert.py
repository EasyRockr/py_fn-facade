from controller.fx_controller import Fx

class ConvertMenu:
    def input_menu(self):
        print("-------------------------------")
        source_currency = input("Source Currency: ").upper()
        target_currency = input("Target Currency: ").upper()
        amount = float(input("Amount: "))
        return source_currency, target_currency, amount

    def convert(self):
        source_currency, target_currency, amount = self.input_menu()
        fx_data = Fx("json").fx_bll.retrieve_rates()
        rates = fx_data.get("rates", {})
        base = fx_data.get("base", "PHP")

        if source_currency == base and target_currency in rates:
            converted = amount / rates[target_currency]
        elif target_currency == base and source_currency in rates:
            converted = amount * rates[source_currency]
        else:
            print("Conversion not available.")
            return

        print(f"{amount:.2f} {source_currency} = {converted:.2f} {target_currency}")
