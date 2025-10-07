import sys
from bll.fx_bll import FxBll

class Fx:
    def __init__(self, source="json"):
        self.fx_bll = FxBll(source)

    def display_rates(self):
        self._do_display_result(self.fx_bll.retrieve_rates().get("rates", {}))

    def _do_display_result(self, rates):
        print("Source Ccy\tTarget Ccy\tRate")
        for src, rate in rates.items():
            print(f"{src}\t\tPHP\t\t{rate}")

    # ----------------------------
    # [2] Convert Money (Strict)
    # ----------------------------
    def convert_money(self):
        data = self.fx_bll.retrieve_rates()
        base = data.get("base", "PHP")
        rates = data.get("rates", {})

        print("\nFx Conversion")
        source = input("Source Ccy: ").strip()

        # Only allow uppercase and valid codes
        valid_ccy = list(rates.keys()) + [base]
        if source not in valid_ccy:
            print("Error")
            sys.exit()  # stop immediately

        target = input("Target Ccy: ").strip()
        amount_str = input(f"Amount in {source}: ").strip()

        try:
            amount = float(amount_str)
        except ValueError:
            print("Error")
            sys.exit()

        # Conversion logic (same as before)
        if source == target:
            print(f"Converted Amt: {amount:.2f} {target}")
            return

        if source == base:
            rate_target = rates.get(target)
            if rate_target is None or rate_target == 0:
                print("Error")
                sys.exit()
            converted = amount / rate_target
        elif target == base:
            rate_source = rates.get(source)
            if rate_source is None:
                print("Error")
                sys.exit()
            converted = amount * rate_source
        else:
            rate_source = rates.get(source)
            rate_target = rates.get(target)
            if rate_source is None or rate_target is None:
                print("Error")
                sys.exit()
            php_amount = amount * rate_source
            converted = php_amount / rate_target

        print(f"Converted Amt: {converted:.2f} {target}")
