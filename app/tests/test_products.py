from flask import request
import unittest
from app.models.products import Product
from app import create_app_environment, app
from app.utils import bp



class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.app = create_app_environment('testing')
        self.app.register_blueprint(bp, url_prefix='/api/v1')

        self.client = self.app.test_client

    def test_admin_or_attendant_can_get_products(self):
        res = self.client().get('http://localhost:5400/api/v1/products')
        self.assertEqual(200, res.status_code)
        self.assertIn('Omo', str(res.data))

    

