from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao
from dal.abstract_contacts import ContactsABC

class ContactBll:
    def get_service_proxy_registry(self):
        return {
            "db": ContactsDbDao(),
            "json": ContactsJsonDao()
        }

    def retrieve_contacts(self, source):
        obj: ContactsABC = self.get_service_proxy_registry().get({source})
        print(obj.__class__.mro())  
        print(isinstance(obj, ContactsABC))
        return obj.retrieve_contacts()
    
    def search_contacts(self, source, keyword):
        obj: ContactsABC = self.get_service_proxy_registry().get({source})
        print(obj.__class__.mro())  
        print(isinstance(obj, ContactsABC))
        return obj.retrieve_contacts()

        
     
        # key = f"retrieve_contacts_{source.lower()}"
        # fn = self.get_service_proxy_registry().get(key)
        # return fn()


        # print(type(obj))
       



