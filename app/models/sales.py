import datetime

from flask import request

from app.utils import get_id, validate_amount, validate_products


class Sale:
    """ stores all the sales made in the store """
    def __init__(self):
        self.sales = []
    
    def get_all_sales(self):
        if len(self.sales) == 0:
            message = {"message":"No sales records yet"}
            return message, 404
        return self.sales, 200

    # def add_sale(self):
    #     data = request.get_json()
    #     sale_record = dict(
    #         sale_id = get_id(self.sales),
    #         attendant_name = data.get("attendant_name"),
    #         products_sold = data.get("products_sold"),
    #         amount_made = data.get("amount_made"),
    #         time_of_sale = datetime.datetime.utcnow()
    #     )
    #     if sale_record in self.sales:
    #         message = {"msg":"sale record already added"}
    #         return  message, 400
    #     self.sales.append(sale_record)
    #     return self.sales
