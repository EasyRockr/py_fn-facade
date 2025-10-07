class ConvertMenu:
    def input_menu(self):
        print("-------------------------------")
        source_currency = input("Source Currency: ")
        target_currency = input("Target Currency: ")
        amount = float(input("Amount: "))
        return source_currency, target_currency, amount


