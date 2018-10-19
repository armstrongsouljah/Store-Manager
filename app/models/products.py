
from flask import request, jsonify, Blueprint
from app.utils import (
    get_id,
    validate_category,
    validate_product_name,
    validate_quantity,
    validate_unitcost,
    validate_id
)


class Product:
    """ stores all the products in the store """

    def __init__(self, **kwargs):
          
        self.products = []  
    
    def add_product(self, **items):
        """ adds products to the store """
        items = request.get_json()
        print(items)
        
        # validate data
        valid_name = validate_product_name(items.get("product_name"))
        valid_category = validate_category(items.get("product_category"))
        valid_quantity = validate_quantity(items.get("quantity"))
        valid_unitcost = validate_unitcost(items.get("unit_cost"))
        # prepare product for addition
        product = dict(
            product_id = get_id(self.products),
            product_name =valid_name,
            product_category = valid_category,
            quantity = valid_quantity,
            unit_cost = valid_unitcost
        )
        if product in self.products:
            message = {"message":"product already added"}
            self.get_products()
            return message
        self.products.append(product)
        return self.products

    def get_products(self):
        """ returns all products in store """
        if len(self.products) == 0:
            message = {"mesage": "no products have been added"}
            return message
        return self.products

    def check_exists(self, id):
        product = [item for item in self.products if item["product_id"]==id]
        if product:
            message = product
        else:
            message = {"msg":"Product not found"}
        return message          

    def get_product(self, id):
        """ returns a single product based off the supplied id """
        id = validate_id(id)
        message = None
        if len(self.products) == 0:
            message = {"msg":"product store is empty"}
        if len(self.products) > 0:
            message = self.check_exists(id)
        return message

