from fastapi import APIRouter
from bll.contacts_bll import ContactBll
from domain.contact import Contact

router = APIRouter(tags=["Contacts API"])
contact_bll = ContactBll("json")

@router.get("/contacts", response_model=list[Contact])
def display_contacts():
    return contact_bll.retrieve_contacts().get("contacts", [])

@router.get("/contacts/search/{keyword}", response_model=list[Contact]) 
def search_contacts(keyword: str):
    return contact_bll.search_contacts(keyword).get("contacts", [])

@router.put("/contacts/create/{name}/{contact_no}")
def create_contacts(name: str, contact_no: str):
    return contact_bll.create_contacts(name, contact_no)

@router.post("/contacts/update/{record_name}/{name}/{contact_no}")
def update_contacts(record_name: str, name: str, contact_no: str):
    return contact_bll.update_contacts(record_name, name, contact_no)

@router.delete("/contacts/delete/{record_name}")
def delete_contact(record_name: str):
    return contact_bll.delete_contacts(record_name)
















# from basepath, we can create
# app = FastAPI(title="Address Book API")

# GraphQL = 
