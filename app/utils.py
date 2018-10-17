import json
from flask import Blueprint


bp = Blueprint('api', __name__)  # needed to enable versioning of my api

def validate_product_name(name):
        if not name:
              raise ValueError("Name can't be blank")
        if name and not isinstance(name, str):
              raise TypeError("Name must be a string")
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
    if not quantity:
          raise ValueError("No quantity added")
    if quantity and not isinstance(quantity, int):
          raise TypeError("quntity must be integer")
    if quantity and quantity == 0:
          raise ValueError("Invalid quantity entered")
    if quantity and quantity < 0:
          raise ValueError("Quantity cannot be negative")
    return quantity

def validate_unitcost(unitcost):
    if not unitcost:
          raise ValueError("No unitcost added")
    if unitcost and not isinstance(unitcost, int):
          raise TypeError("unitcost must be integer")
    if unitcost and unitcost == 0:
          raise ValueError("Invalid unitcost entered")
    if unitcost and unitcost < 0:
          raise ValueError("unitcost cannot be negative")
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
