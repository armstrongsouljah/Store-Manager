
from flask import  request, abort

from app.utils import (get_collection,  get_item_id,
                       is_empty,  validate_entry, validate_product_entries)


class Product:
    """ stores all the products in the store """

    def __init__(self, **kwargs):
          
        self.products = []
          
    def add_product(self, **items):
        """ adds products to the store """
        items = request.get_json()

        product_name = items.get("product_name")
        product_category = items.get("product_category")
        product_quantity = items.get("quantity")
        product_unitcost = items.get("unit_cost")

        # prepare product for addition
        product = dict(
            product_id = get_item_id('product_id', self.products),
            product_name = product_name,
            product_category = product_category,
            quantity = product_quantity,
            unit_cost = product_unitcost
        )

        existing_item = [item for item in self.products if item["product_name"] == product_name ]
        validation_errors = validate_product_entries(
            product_name=product_name,
            product_category=product_category,
            quantity=product_quantity,
            unit_cost=product_unitcost
        )

        if validation_errors:
            return validation_errors

        
        
        if not is_empty(existing_item):
            message = {"message":"Product already exists"}
            return message
        else:
            self.products.append(product)
            message = {"msg":"Product was created successfully!"}
        return message

    @property
    def get_products(self):
        return get_collection(self.products)

    def get_product(self, product_id):
        """ returns a single product based off the supplied id """
        product_id = validate_entry(product_id, int)

        returned_product = [product for product in self.products if product["product_id"] == product_id]
        if is_empty(returned_product):
            message = {'msg': 'Product not found'}
            return message
        else:
            message = returned_product[0]
        return message

    def update_product_details(self, product_id):
        """ check for the product in store """
        data = request.get_json()
        unit_cost = validate_entry(data.get("unit_cost"), int)       
        
        product = [item for item in self.products if item['product_id']==product_id]
        if is_empty(product):
            message ={'msg':'Item doesnot exist'}
    
        if not is_empty(product) and unit_cost:
            product[0]['unit_cost'] = unit_cost
            message = {'msg':'Updated successfully'}
        else:
            abort(400, "Invalid data not allowed")
        return message

    def delete_from_store(self, product_id):

        item = [product for product in self.products if product['product_id']==product_id]

        if is_empty(item):
            message ={'msg':'Item doesnot exist'}
    
        if not is_empty(item):
            self.products.remove(item[0])
            message = {'msg':'Item removed successfully'}                                        
        return message
