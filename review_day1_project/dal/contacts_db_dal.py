from dal.db_dal import DbDaoABC
from dal.abstract_contacts import ContactsABC

class ContactsDbDao(DbDaoABC, ContactsABC):
    def retrieve_contacts(self):
        sql = "SELECT name, contact FROM contacts"
        result = {"contacts": []}

        for row in self.execute_select(sql):
            result["contacts"].append({
                "name": row[0],
                "contact_no": row[1]
            })

        return result

    # def search_contacts(self, keyword):
    #     sql = "SELECT name, contact FROM contacts WHERE name LIKE ?"
    #     result = {"contacts": []}
    #     for row in self.execute_select(sql, (f"%{keyword}%",)):
    #         result["contacts"].append({
    #             "name": row[0],
    #             "contact_no": row[1]
    #         })
    #     return result




# import sqlite3
# import os

# def get_db_connection():
#     base_dir = os.path.dirname(__file__)
#     db_path = os.path.join(base_dir, "..", "address_book1.db")
#     db_path = os.path.abspath(db_path)
#     return sqlite3.connect(db_path)

# def retrieve_contacts():
#     sql = "SELECT name, contact FROM contacts"
#     cnn = get_db_connection()
#     cursor = cnn.execute(sql)
#     result = {"contacts": []}
#     for row in cursor:
#         result["contacts"].append({
#             "name": row[0],
#             "contact_no": row[1]
#         })
#     cnn.close()
#     return result
