import datetime

from flask import request

from app.utils import (get_id, validate_amount, validate_attendant,
                       validate_id, validate_products)


class Sale:
    """ stores all the sales made in the store """
    def __init__(self):
        self.sales = [
            { 'sale_id':1,
                'attendant_name':"Mwesigye",
                'products_sold':[{"milk":12000}, {"chicken":18000}],
                'amount_made':30000,
                'time_of_sale':"23, 9, 2018"
            }
        ]
    
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

    def get_sale_by_id(self, id):
        """ gets a sales record if that id exists """
        # id = validate_id(id)

        for record in self.sales:
            if record["sale_id"] == id:
                response = record, 200
                return response
            return "Record with that id doesnot exist!", 404
