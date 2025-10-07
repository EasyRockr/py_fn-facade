from dal.fx_dal import FxJsonDao
from dal.abstract_fx import FxABC

class FxFactory:
    def create_instance(self, source: str) -> FxABC:
        obj_map = {
            "json": FxJsonDao
        }
        dao_class = obj_map.get(source)
        if dao_class is None:
            raise Exception("Invalid Source")
        return dao_class()
