class ContactsABC:
    def retrieve_contacts(self):
        pass

    def search_contacts(self, keyword):
        pass

    def create_contacts(self, name, contact):
        pass

    def update_contacts(self, record_name, name, contact):
        pass

    def delete_contacts(self, record_name):
        pass
