import json
import string
from flask import  Blueprint, jsonify, request

from app.config import DevelopmentConfig

dev = DevelopmentConfig()
bp = Blueprint('api', __name__)  # needed to enable versioning of my api

def validate_product_change_details(quantity, unit_cost):
    error_message = None
    if not quantity:
            error_message = {'error': 'Missing quantity'}

    if quantity and not isinstance(quantity, int):
        error_message = {'error': 'quantity must be an integer'}

    if not unit_cost:
        error_message = {'error': 'Please enter unit_cost'}

    if unit_cost and not isinstance(unit_cost, int):
        error_message = {'error':'unit cost must be a number'}
    
    if error_message:
        return error_message


def validate_sale_record(productid, quantity):
    error_message = None        
    if not productid or not quantity:
        error_message = {'error': 'Product or quantity cannot be empty'}
    if not isinstance(productid, int): 
        error_message = {'error': 'Product  must be a number.'}
    if not isinstance(quantity, int):
        error_message = {'error': 'quantity must be a number'}
    if quantity == 0 or productid == 0:
        error_message = {'error': 'Invalid for product or quantity'}
    if error_message:
        return error_message
    return None



def validate_product_entries(product_name, quantity, unit_cost):

    message = None

    if not product_name or not unit_cost or not quantity:
            message = {'message': "productname/ unitcost or quantity can't be blank"}

    if product_name =="" or product_name ==" ":
        message = {'message': 'Product cannot be empty'}

    if not isinstance(product_name, str):
        message = {'message':'Product name must be a string'}

    if not isinstance(quantity, int) or not isinstance(unit_cost, int):
        message = {'message': 'quantity/unitcost must be intergers'}  

    if isinstance(quantity, int) and quantity < 1 \
    or isinstance(unit_cost, int) and unit_cost < 1:
        message = {'message':'quantity/unitcost must be above zero'}
    if message:
        return message


def fetch_all(relation, db_cursor):
    query = f"""
      SELECT * FROM {relation}
      """
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    if result:
        return result    
    return  {'message': 'No records in store'}

def validate_registration_data(username, password,role):
    message = None
    if not username or not password or not role:
        message = {'mesage':'username/password fields not allowed'}
    if username == "" or username ==" " or password == "":
        message = {'message':'username/password cannot be spaces'}
    if username and not username.isalpha():
        message = {'message': 'Username must only be alphabetical letters'}
    if username and username[0] in string.digits:
        message = {'message':'Username/password cannot startwith a number'}

    if not isinstance(username, str) or not isinstance(password, str):
        message = {'message': 'Username/password must be a word'}
    if not isinstance(role, str):
        message = {'message': 'User role must be a string'}
    if role and not role.isalpha():
        message = {'message': 'User role must only contain alphabets'}

    if username and len(username) < 5 or password and len(password) < 5:
        message = {'message': 'Username/password must be 6 characters and above'}
    return message





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

