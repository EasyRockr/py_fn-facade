from util.file_util import read_json_as_dict
from dal.abstract_contacts import ContactsABC

class ContactsJsonDao(ContactsABC):
    def retrieve_contacts(self):
        return read_json_as_dict("contacts.json")
    
    def search_contacts(self, keyword):
        data = self.retrieve_contacts()
        result = {"contacts": []}
        for record in data.get("contacts", []):
            if keyword.lower() in record.get("name", "").lower():
                result["contacts"].append(record)
        return result
