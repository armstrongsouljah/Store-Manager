from flask import jsonify, request, Blueprint


class Product:
    """ stores all the products in the store """

    
    def __init__(self):
        self.products = [
            {
                'product_id':1,
                'product_name': 'Omo',
                'product_category': 'Detergents',
                'quantity': 3000,
                'minimum_quantity': 120,
                'unit_cost': 4500,
                'date_added': '23,09,2018'
            },
            {
                'product_id': '2',
                'product_name': 'LG Microwave',
                'product_category': 'Electronics',
                'quantity': 160,
                'minimum_quantity': 7,
                'unit_cost': 450000,
                'date_added': '28,07,2018'
            }
        ]
    
    def get_products(self):
        if len(self.products) == 0:
            # return jsonify({"message": "no products added yet."}), 404
            return "No products in store!"
        else:
            # return jsonify(self.products), 200
            return self.products
