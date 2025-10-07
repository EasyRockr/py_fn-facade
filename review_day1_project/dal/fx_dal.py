from file.file_util import read_json_as_dict
from dal.abstract_fx import FxABC

class FxJsonDao(FxABC):
    def retrieve_rates(self):
        return read_json_as_dict("rates.json")
    
    
