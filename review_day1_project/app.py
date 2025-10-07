from controller.address_book import Contacts

try:
    Contacts("db").display_contacts()
    Contacts("db").search_contacts("Jane")
except Exception as ex:
    print(f"Error in starting application: {str(ex)}")

# oltp
# put try catch in the main point, return business validation

