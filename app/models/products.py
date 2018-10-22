
from flask import request, jsonify, Blueprint
from app.utils import (
    check_exists,
    get_id,
    get_item_id,
    get_collection,
    is_empty,
    validate_category,
    validate_product_name,
    validate_quantity,
    validate_unitcost,
    validate_id
)


class Product:
    """ stores all the products in the store """
    id = None
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
            product_id = get_item_id('product_id', self.products),
            product_name =valid_name,
            product_category = valid_category,
            quantity = valid_quantity,
            unit_cost = valid_unitcost
        )
        
        if product in self.products:
            message = {"message":"product already added"}
        self.products.append(product)
        message = {"msg":"Product was created successfully!"}
        return message

    @property
    def get_products(self):
        return get_collection(self.products)

    def get_product(self, product_id):
        """ returns a single product based off the supplied id """
        product_id = validate_id(product_id)
        if len(self.products) == 0:
            message = {"msg":"product store is empty"}
        if len(self.products) > 0:
            message = check_exists("product_id", self.products, product_id)
        return message

    def update_product_details(self, product_id):
        """ check for the product in store """
        data = request.get_json()
        unit_cost = validate_unitcost(data.get("unit_cost"))       
        # item_id = validate_id(product_id)
        message = None
        if is_empty(self.products):
            message = {"msg": "No products in store"}
        else:
            for item in self.products:
                if item['product_id'] != product_id:
                    message = {'msg': 'Product not found'}
                else:                    
                    item.update({'unit_cost': unit_cost})
                    message = {'msg': 'Updated successfully'}
        return message

    def delete_from_store(self, product_id):

        if is_empty(self.products):
            message = {"msg": "No products in store"}
        else:
            for item in self.products:
                if item['product_id'] != product_id:
                    message = {'msg': 'Item doesnot exist'}                    
                else:
                    self.products.remove(item)
                    message = {'msg':'Item successfully removed'}
                    
        return message
