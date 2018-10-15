from flask import jsonify, request


class Product:
    """ stores all the products in the store """

    
    def __init__(self):
        self.products = [
            {
                'product_id':'1',
                'product_name': 'Omo',
                'product_category': 'Detergents',
                'quantity': '3000 pcs',
                'minimum_quantity': '120 pcs',
                'date_added': '23,09,2018'
            }
        ]
    
    def get_products(self):
        if len(self.products) == 0:
            return jsonify({"message": "no products added yet."}), 200
        else:
            return jsonify(self.products), 200
