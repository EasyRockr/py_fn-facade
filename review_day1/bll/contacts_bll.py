from dal.contacts_dal import retrieve_contacts as retrieve_contacts_json
from dal.contacts_db_dal import retrieve_contacts as retrieve_contacts_db

def get_service_proxy_registry():
    return {
        "retrieve_contacts_db" : retrieve_contacts_db(),
        "retrieve_contacts_json" : retrieve_contacts_json()
    }

def retrieve_contacts(source):
    return get_service_proxy_registry().get(f"retrieve_contacts_{source}")()



"""
MVC


views - eto lang mababago
BE - the model wont change
"""

# dal any data-retrieval
# bll - any business function / logic (check age, check if nandon record)
# - cannot have any sql statements, no api reqs, just extracts the dal ()
# kunin mo yung function sa data layer
# fastapi add? makukuha ko na s bll yung data so i just need to create a file for fastapi


# controller - entry point of the app



# this is a command pattern (design pattern)
    # dito lang magagalaw




    # def retrieve_contacts(source):
    # if source == "db":
    #     return retrieve_contacts_json()
    # else:
    #     return retrieve_contacts_json()
    # # dito lang magagalaw