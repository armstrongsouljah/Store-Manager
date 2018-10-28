import json
import string
from flask import  Blueprint, jsonify, request

from app.config import DevelopmentConfig

dev = DevelopmentConfig()
bp = Blueprint('api', __name__)  # needed to enable versioning of my api


def validate_id(id):
    if not isinstance(id, int):
        raise TypeError("Id should be a number")
    return id



def validate_entry(item, item_type):
    if not item:
        raise AssertionError("Empty value is not allowed.")
    
    if item and not isinstance(item, item_type):
        raise TypeError("Invalid data type supplied.")
    
    if item and isinstance(item, int) and item == 0:
        raise ValueError("Invalid data supplied.")
    return True 



def validate_product_entries(product_name, product_category, quantity, unit_cost):

    message = None

    if not product_name or not product_category or not quantity or not unit_cost:
        message = {"message": "Empty records not allowed"}
    
    if not isinstance(product_name, str) or not isinstance(product_category, str):
        message = {"message":"Product name  or category must be of type string"}
        

    if not isinstance(quantity, int) or not isinstance(unit_cost, int):
        message = {"message":"Quantity or unit cost must be of a number"}
      
    if message:
        return message
    return None


def validate_sales_data(products,amount, attendant):
    response = None

    if not attendant or not amount or not products:
        response = {'error':'Not allowed to add empty values'}
        
    if not isinstance(attendant, str):
        response = {'error': 'Attendant must be of type string'}
        # return response
    if not isinstance(products, list):
        response = {'error': 'Items must be a collection'}
        # return response
    if not isinstance(amount, int):
        response = {'error':'Amount must be in numbers'}
        # return response
    if response:
        return response
    return None




welcome_message = """
   <!DOCTYPE html>
     <html>
       <head>
         <title>Store Manager API</title>
         <style type='text/css'>
           *{
               margin:0;
               padding:0;
           }
           body{
               width:80%;
               margin:0 auto;
           }
           .main-container{
               margin-top:45px;
           }
           h2{
               font-size:16pt;
               color:orange;
               text-align:center;
           }
           a{
               text-decoration:none;
           }
         </style>
       </head>
       <body>
         <div class='main-content'>
           <h2>Store Manager</h2>
              Currently supported endpoints <br>
              <a href='https://soultech-store.herokuapp.com/api/v1/products'>Products</a> <br/>
              <a href='https://soultech-store.herokuapp.com/api/v1/sales'>Sales</a>
         </div>
       </body>
     </html>
"""




def is_empty(item_list):
    if len(item_list) == 0:
        return True
    return False


def check_exists(entry_name, item_list):
    item = [entry for entry in item_list if entry.get(entry_name) == entry_name]
    if is_empty(item):
        message = False
    else:
        message = True
    return message

# returns a collection of items
def get_collection(item_list):
    """ Returns items to the user based on the list supplied """
    if is_empty(item_list):
        response = {"msg":"No records yet."}
    else:
        response = item_list
    return response



def get_id(list):
      length = len(list)
      return length + 1


def get_item_id(item_id, item_list):
        if not is_empty(item_list):
            last_item = item_list[-1]
            id = last_item.get(item_id) + 1
        else:
            id = 1
        return id


def validate_username(username):
        if len(username) < 5:
            raise ValueError("username must be 5 and above characters")
            
        if username == " ":
            raise ValueError("Name cannot be spaces")

        if not isinstance(username, str):
            raise TypeError("Username must be a string")

        if username.startswith(string.digits):
            raise ValueError("Username cannot start with a number")
        return username
