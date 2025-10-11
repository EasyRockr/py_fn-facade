from dal.contacts_dal import retrieve_contacts

def display_contacts():
    print(retrieve_contacts())
    for record in retrieve_contacts().get("contacts", []):
        print(f"{record.get("name", "")} \t\t {record.get("contact_no")}")

display_contacts()