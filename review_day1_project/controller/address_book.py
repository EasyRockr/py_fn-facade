from bll.contacts_bll import ContactBll


class Contacts:
    def __init__(self):
        print("## init!")
        self.contact_bll = ContactBll()
    def display_contacts(self, source):
        print("## display_contacts!")
        data = self.contact_bll.retrieve_contacts(source)
        for record in data.get("contacts", []):
            print(f"{record.get('name', '')}\t\t{record.get('contact_no', '')}")
