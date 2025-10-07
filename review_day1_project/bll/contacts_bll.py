from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao
from dal.abstract_contacts import ContactsABC

class ContactBll:
    def get_service_proxy_registry(self):
        return {
            "db": ContactsDbDao(),
            "json": ContactsJsonDao()
        }

    def get_service(self, source) -> ContactsABC:
        obj = self.get_service_proxy_registry().get(source)
        print(obj.__class__.mro())
        print(isinstance(obj, ContactsABC))
        return obj

    def retrieve_contacts(self, source):
        return self.get_service(source).retrieve_contacts()

    def search_contacts(self, source, keyword):
        return self.get_service(source).search_contacts(keyword)
