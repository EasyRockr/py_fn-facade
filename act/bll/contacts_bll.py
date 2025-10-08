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

    def create_contacts(self, keyword: str):
        return self.contact_dao.create_contacts(keyword)