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

@router.get("/contacts/create/{keyword}", response_model=list[Contact])
def create_contacts(keyword: str):
    return contact_bll.create_contacts(keyword).put("contacts", [])
















# from basepath, we can create
# app = FastAPI(title="Address Book API")

# GraphQL = 
