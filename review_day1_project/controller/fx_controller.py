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
