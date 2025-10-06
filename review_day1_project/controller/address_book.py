from bll.contacts_bll import retrieve_contacts

def display_contacts(source):
    data = retrieve_contacts(source)
    for record in data.get("contacts", []):
        print(f"{record.get('name', '')}\t\t{record.get('contact_no', '')}")
