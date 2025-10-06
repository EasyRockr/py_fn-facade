from dal.contacts_dal import retrieve_contacts as retrieve_contacts_json
from dal.contacts_db_dal import retrieve_contacts as retrieve_contacts_db

def get_service_proxy_registry():
    return {
        "retrieve_contacts_db": retrieve_contacts_db,
        "retrieve_contacts_json": retrieve_contacts_json
    }

def retrieve_contacts(source):
    key = f"retrieve_contacts_{source.lower()}"
    fn = get_service_proxy_registry().get(key)
   
    return fn()
