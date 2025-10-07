from dal.abstract_fx import FxABC
from dal.dal_factory import FxFactory

class FxBll:
    __fx_dao: FxABC

    def __init__(self, source: str):
        self.__fx_dao = FxFactory().create_instance(source)

    def retrieve_rates(self):
        return self.__fx_dao.retrieve_rates()
