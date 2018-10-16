
from flask import jsonify, request, Blueprint


class Product:
    """ stores all the products in the store """

    
    def __init__(self, **kwargs):
        self.product_name = kwargs.get("product_name")
        self.product_category = kwargs.get("product_category")
        self.quantity = kwargs.get("quantity") 
        self.unit_cost = kwargs.get("unit_cost")
        self.date_added = kwargs.get("date_added")   
        self.products = [
            {
                "product_id": 1, 
                "product_name":"Lg Flat Screen", 
                "product_category": "Electronics",
                "quantity":545, 
                "unit_cost":230000, 
                "date_added": "23,09.2017"
            },
            {
                "product_id": 2, 
                "product_name":"Omo", 
                "product_category": "Detergents",
                "quantity":120, 
                "unit_cost":2300, 
                "date_added": "23,09.2017"
            }
        ]
    
    def get_products(self):
        if len(self.products) == 0:
            # return jsonify({"message": "no products added yet."}), 404
            message = {"mesage": "no products have been added"}
            return message
        else:
            # return jsonify(self.products), 200
            return self.products
