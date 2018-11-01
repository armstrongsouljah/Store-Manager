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



def validate_product_entries(product_name, quantity, unit_cost):

    message = None

    if not product_name or not unit_cost or not quantity:
            message = {'msg': "productname/ unitcost or quantity can't be blank"}

    if product_name =="" or product_name ==" ":
        message = {'msg': 'Product cannot be an empty space'}

    if not isinstance(product_name, str):
        message = {'msg':'Product name must be a string'}

    if not isinstance(quantity, int) or not isinstance(unit_cost, int):
        message = {'msg': 'quantity/unitcost must be intergers'}  

    if isinstance(quantity, int) and quantity < 1 \
    or isinstance(unit_cost, int) and unit_cost < 1:
        message = {'msg':'quantity/unitcost must be above zero'}
    if message:
        return message


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

def fetch_all(relation, db_cursor):
    q = f"""
      SELECT * FROM {relation}
      """
    db_cursor.execute(q)
    result = db_cursor.fetchall()
    if result:
        return result    
    return  {'msg': 'No records in store'}
    



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
