import json
from flask import Blueprint, request, jsonify
from functools import wraps
import jwt
from app.config import DevelopmentConfig


dev = DevelopmentConfig()
bp = Blueprint('api', __name__)  # needed to enable versioning of my api
 
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing'}), 403

        try:
            data = jwt.decode(token,
            dev.SECRET_KEY)
        except Exception  as E:
            return jsonify({
            'message':'TOken is missing or invalid',
      }), 403
        return f(*args, **kwargs)
    return decorated
    


def validate_id(id):
    if not isinstance(id, int):
        raise TypeError("Id should be a number")
    return id

def validate_type(item, type):
    if not isinstance(item, type):
        raise TypeError(f"item should be of type {type.__class__}")
    return True

def validate_product_name(name):
    validate_type(name, str)
    if name and name =="" and name ==" ":
        raise ValueError("Name can't be spaces")
    return name

def validate_category(category):
    if not category:
              raise ValueError("category can't be blank")
    if not isinstance(category, str):
          raise TypeError("Name must be a string")
    if category and category =="" and category ==" ":
          raise ValueError("category can't be spaces")
    return category
    
def validate_quantity(quantity):
    if quantity and not isinstance(quantity, int):
          raise TypeError("quntity must be integer")
    if quantity and quantity == 0:
          raise ValueError("Invalid quantity entered")
    if quantity and quantity < 0:
          raise ValueError("Quantity cannot be negative")
    return quantity

def validate_unitcost(unitcost):
    validate_type(unitcost, int)
    if unitcost and unitcost <= 0:
          raise ValueError("Invalid unitcost entered")    
    return unitcost

def get_id(list):
      length = len(list)
      return length + 1

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
              <a href='/api/v1/products'>products</a>
         </div>
       </body>
     </html>
"""
# sales validations
def validate_attendant(name):
    if name and not isinstance(name, str):
        raise TypeError("Name mus be a string")
    return name

def validate_products(products):
    if products and not isinstance(products, list):
        raise TypeError("Name mus be a list")
    return products

def validate_amount(amount):
    if amount and not isinstance(amount, int):
        raise TypeError("Amount must be numbers")

    if amount <= 0:
        raise ValueError("Invalid amount")
    return amount

def check_exists(item_id, item_list, id):
        _item = [item for item in item_list if item[item_id]==id]
        if _item:
            message = _item
        else:
            message = {"msg":"Item not found"}
        return message 