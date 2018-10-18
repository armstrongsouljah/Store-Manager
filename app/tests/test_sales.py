import json
import unittest

from flask_jwt_extended import create_access_token, JWTManager

from app import app, create_app_environment, jwt
from app.config import BaseConfig
from app.models.sales import Sale
from app.utils import bp

class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app = create_app_environment('testing')
        self.app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY
        self.app.register_blueprint(bp, url_prefix='/api/v1')
        self.jwt = JWTManager(self.app)
        self.client = self.app.test_client(self)
        self.sales_uri = 'api/v1/sales'

    def test_admin_can_get_sales(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.get(
                self.sales_uri,
                headers=headers,
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(200, res.status_code)
