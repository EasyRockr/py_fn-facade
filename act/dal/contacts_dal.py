from util.file_util import read_json_as_dict, write_dict_as_json
from dal.abstract_contacts import ContactsABC

class ContactsJsonDao(ContactsABC):
    def retrieve_contacts(self):
        return read_json_as_dict("contacts.json")
    
    def search_contacts(self, keyword):
        data = self.retrieve_contacts()
        result = {"contacts": []}
        for record in data.get("contacts", []):
            if keyword.lower() in record.get("name", "").lower():
                result["contacts"].append(record)
        return result

    def create_contacts(self, name, contact_no):
        data = self.retrieve_contacts()
        new_contact = {"name": name, "contact_no": contact_no}
        data.setdefault("contacts", []).append(new_contact)
        write_dict_as_json("contacts.json", data)
        return {"message": "Contact added successfully"}

    def update_contacts(self, record_name, name, contact):
        data = self.retrieve_contacts()
        for r in data.get("contacts", []):
            if r["name"].lower() == record_name.lower():
                r.update({"name": name, "contact_no": contact})
                write_dict_as_json("contacts.json", data)
                return {"message": f"Contact '{record_name}' updated successfully."}
        return {"error": f"Contact '{record_name}' not found."}

    def delete_contacts(self, record_name):
        matches = self.search_contacts(record_name).get("contacts", [])
        if not matches:
            return {"error": f"Contact '{record_name}' not found."}

        data = self.retrieve_contacts()
        for r in matches:
            data["contacts"].remove(r)
        write_dict_as_json("contacts.json", data)
        return {"message": f"Contact '{record_name}' deleted successfully."}











# def delete_contacts(self, record_name):
#     data = self.retrieve_contacts()
#     for r in data.get("contacts", []):
#         if r["name"].lower() == record_name.lower():
#             data["contacts"].remove(r)
#             write_dict_as_json("contacts.json", data)
#             return {"message": f"Contact '{record_name}' deleted successfully."}
#     return {"error": f"Contact '{record_name}' not found."}




    # def update_contacts(self, record_name, name, contact):
    #     data = self.retrieve_contacts()
    #     search_result = self.search_contacts(record_name).get("contacts", [])
    #     if not search_result:
    #         return {"error": f"Contact '{record_name}' not found."}

    #     for record in data.get("contacts", []):
    #         if record.get("name").lower() == record_name.lower():
    #             record["name"] = name
    #             record["contact_no"] = contact
    #             break

    #     write_dict_as_json("contacts.json", data)
    #     return {"message": f"Contact '{record_name}' updated successfully."}

