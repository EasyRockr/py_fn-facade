from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao
from dal.abstract_contacts import ContactsABC

class ContactsFactory:
    def create_instance(self, source: str) -> ContactsABC:
        obj_map = {
            "db": ContactsDbDao,
            "json": ContactsJsonDao
            # "api" : ContactsApiDao
        }

        dao_class = obj_map.get(source)
        if dao_class is None:
            raise Exception("Invalid Source")

        return dao_class()
