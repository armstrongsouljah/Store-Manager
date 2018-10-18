import datetime

from flask import request

from app.utils import get_id, validate_amount, validate_products, validate_attendant


class Sale:
    """ stores all the sales made in the store """
    def __init__(self):
        self.sales = []
    
    def get_all_sales(self):
        if len(self.sales) == 0:
            message = {"message":"No sales records yet"}
            return message, 404
        return self.sales, 200

    def add_sale(self):
        data = request.get_json()
        amount = validate_amount(data.get("amount_made"))
        products = validate_products(data.get("products_sold"))
        attendant = validate_attendant(data.get("attendant_name"))
        
        sale_record = dict(
            sale_id = get_id(self.sales),
            attendant_name = attendant,
            products_sold = products,
            amount_made = amount,
            time_of_sale = datetime.datetime.utcnow()
        )
        if sale_record in self.sales:
            message = {"msg":"sale record already added"}
            return  message, 400
        self.sales.append(sale_record)
        return self.sales
