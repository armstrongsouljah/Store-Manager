import json
import unittest

from flask import request
from flask_jwt_extended import JWTManager, create_access_token

from app import app, create_app_environment, jwt
from app.config import BaseConfig
from app.models.products import Product
from app.utils import bp


class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.app = create_app_environment('testing')
        self.app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY
        self.app.register_blueprint(bp, url_prefix='/api/v1')
        self.product_obj = Product()
        self.jwt = JWTManager(self.app)
        self.products  = self.product_obj.products
        self.client = self.app.test_client(self)
        self.product_uri = 'api/v1/products'
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
        data = json.loads(res.data)
        self.assertEqual(200, data[-1], msg="found product")

    def test_can_get_specific_product(self):
        id = 1
        
        res = self.client.get(
            'api/v1/products/%d' %id,
            content_type='application/json'
        )
        data = json.loads(res.data)
        self.assertEqual(200, data[-1], msg="found product")

    def test_cannot_get_non_existent_id(self):
        id = 3
        self.product_uri = "http://localhost:5400/api/v1/products/%d" %id
        res = self.client.get(self.product_uri)
        print(res.data)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(404, data[-1], msg="Must equal 404")
       
    def test_admin_can_add_product(self): 
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
            self.assertEqual(200, res.status_code)

    def test_admin_can_add_valid_category(self):        
        with self.app.app_context():
            self.sample_product["product_category"] = 23233
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
        # print(res.data)
        print(res.status_code)
        self.product_obj.get_products()  
        self.assertEqual(500, res.status_code)


    def test_admin_dont_add_empty_product(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}   
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.empty_product)
            )
        self.assertEqual(500, res.status_code)
        
        
    
    def tearDown(self):
        self.app = None
        self.product_obj = None
        self.client = None
