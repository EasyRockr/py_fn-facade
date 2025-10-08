from fastapi import FastAPI
from controller.address_book_api import router as address_book_router
from controller.country_api import router as country_router

app = FastAPI()
api_app = FastAPI()

api_app.include_router(address_book_router)
api_app.include_router(country_router)

app.mount("/api/v1", api_app)



#http://127.0.0.1:8000/api/v1/docs
# irouroute sa nginx

# graphql = parang sql, supports strawberry graphql
# 















# #  Mount the address_book_api routes under same root path
# app.mount("", address_book_api)

# # -------------------------------
# # ITEM ROUTES
# # -------------------------------
# @app.put("/item")
# def add_item(item: Item):
#     return "Item Added"

# @app.post("/item")
# def update_item():
#     return "Item Updated"

# @app.get("/item")
# def get_item():
#     return "Sample Item"

# @app.delete("/item")
# def delete_item():
#     return "Item Deleted"

# 1 engdpoint = multiple operations





# from fastapi import FastAPI # this is a module

# app = FastAPI()

# # decorator pattern = add functionalities methods to the function. extends the fn of the greet function to a restful function
# # get is the http method
# @app.get("/greet") 
# def greet():
#     return "Hello From FastAPI!!!"


# # http://127.0.0.1:8000/docs