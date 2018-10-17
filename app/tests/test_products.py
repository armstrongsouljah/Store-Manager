from flask import request
import json
import unittest
from flask_jwt_extended import JWTManager
from app.models.products import Product
from app import create_app_environment, app
from app.utils import bp
from app import jwt
from app.config import BaseConfig

class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.app = create_app_environment('testing')
        # self.app.config['JWT_TOKEN_LOCATION'] = BaseConfig.JWT_TOKEN_LOCATION
        self.app.register_blueprint(bp, url_prefix='/api/v1')
        self.product_obj = Product()
        self.jwt = jwt
        self.products  = self.product_obj.products
        self.client = self.app.test_client(self)
        self.product_uri = 'api/v1/products'
        self.admin_uri = 'http://localhost:5400/api/v1/admin/products/'
        self.sample_product = dict(
            product_name = "Cooker",
            product_category="Electronics",
            quantity=37,
            unit_cost=13000000
        )

        self.empty_product = dict(
            product_name = "",
            product_category="",
            quantity=None,
            unit_cost=None
        )

    

    def test_admin_or_attendant_can_get_products(self):
        res = self.client.get(self.product_uri)
        self.assertEqual(200, res.status_code)
        
    def test_admin_can_add_product(self): 
        # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mzk3NzU0OTUsIm5iZiI6MTUzOTc3NTQ5NSwianRpIjoiZTMwNzhhZDItY2YzYy00YTc4LTlhMTAtMWRlODllZjgzZjliIiwiZXhwIjoxNTQwMzgwMjk1LCJpZGVudGl0eSI6ImFybXN0cm9uZyIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.5OnHbfnBe7U7r0j46LC3-1MvitUEbBUHYvfZ_DpqnAg"      
        res = self.client.post(
            self.admin_uri,
            content_type='application/json',
            # headers={'Authorization':f'Bearer {token}'},
            data=json.dumps(self.sample_product)
        )
        print(res.data)
        print(res.status_code)
        self.product_obj.get_products()  
        self.assertEqual(200, res.status_code)

    def test_admin_dont_add_empty_product(self):
        res = self.client.post(
            self.admin_uri,
            content_type='application/json',
            # headers={'Authorization':f'Bearer {token}'},
            data=json.dumps(self.empty_product)
        )
        self.assertEqual(500, res.status_code)
        
        
    
    def tearDown(self):
        self.app = None
        self.product_obj = None
        self.client = None



    

