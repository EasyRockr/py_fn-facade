from dal.abstract_contacts import ContactsABC
from dal.dal_factory import ContactsFactory

class ContactBll:
    __contact_dao: ContactsABC

    def __init__(self, source: str):
        self.__contact_dao = ContactsFactory().create_instance(source)

    def retrieve_contacts(self):
        return self.__contact_dao.retrieve_contacts()

    def search_contacts(self, keyword: str):
        return self.__contact_dao.search_contacts(keyword)

    def create_contacts(self, name:str, contact_no:str):
        return self.__contact_dao.create_contacts(name, contact_no)
    
    def update_contacts(self, record_name, name, contact_no):
        return self.__contact_dao.update_contacts(record_name, name, contact_no)
    
    def delete_contacts(self, record_name):
        return self.__contact_dao.delete_contacts(record_name)