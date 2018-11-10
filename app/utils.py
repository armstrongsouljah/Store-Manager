import json
import string
from flask import  Blueprint, jsonify, request

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
    if quantity and isinstance(quantity, int) <= 0 or productid == 0:
        error_message = {'error': 'Invalid input for stock or product'}
    if error_message:
        return jsonify(error_message), 400
    return None



def validate_product_entries(product_name, category, quantity, unit_cost):

    message = None

    if not product_name or not unit_cost or not quantity or not category:
            message = {'message': "productname/ unitcost or quantity or category can't be blank"}

    if product_name =="" or product_name ==" ":
        message = {'message': 'Product cannot be empty'}

    if not isinstance(product_name, str):
        message = {'message':'Product name must be a string'}

    if not isinstance(quantity, int) or not isinstance(unit_cost, int) or not isinstance(category, int):
        message = {'message': 'quantity/unitcost/category must be intergers'}  

    if isinstance(quantity, int) and quantity < 1 \
    or isinstance(unit_cost, int) and unit_cost < 1:
        message = {'message':'quantity/unitcost must be above zero'}
    if message:
        return jsonify(message), 400


def fetch_all(relation, db_cursor):
    query = f"""
      SELECT * FROM {relation}
      """
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    if result:
        return jsonify(result), 200    
    return  jsonify({'message': 'No records in store'}), 400


def fetch_details_by_id(column_name, column_value, relation, db_cursor):
    fetch_item_query = f"""
       SELECT * FROM {relation} WHERE {column_name}='{column_value}'
    """
    db_cursor.execute(fetch_item_query)
    returned_item = db_cursor.fetchone()
    if returned_item:
        response = jsonify(returned_item), 200
    else:
        response = jsonify({'message':f'{relation} item not found'}), 404
    return response

def remove_entry_by_id(column_name, relation, entry_id, db_cursor):
    delete_entry_query = f"""
    DELETE FROM {relation} WHERE {column_name}='{entry_id}'
    """

    try:
        db_cursor.execute(delete_entry_query)
        response = jsonify({'message': 'Item successfully deleted.'}), 202
    except Exception as error:
        response = jsonify({'message': f'query failed due {error}'}), 400
    return response

def validate_registration_data(username, password,role):
    message = None
    if not username or not password or not role:
        message = {'mesage':'empty username/password and role fields not allowed'}
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


def check_item_exists(column_name, relation, column_value, db_cursor):
    check_existence_query = f"""
       SELECT {column_name} FROM {relation} WHERE {column_name}='{column_value}'
    """

    db_cursor.execute(check_existence_query)

    returned_row = db_cursor.fetchone()
    if returned_row:
        return returned_row
    else:
        return None

def validate_category_name(categoryname):
    error_message = None
    if not categoryname:
        error_message = {'message': 'Category cannot be blank'}
    if categoryname and not isinstance(categoryname, str):
        error_message = {'message': 'Category name accepts string characters'}
    if categoryname and isinstance(categoryname, str) and not categoryname.isalpha():
        error_message = {'message': 'Category should only contain alphabetical characters.'}
    
    if error_message:
        return error_message
    else:
        return None



