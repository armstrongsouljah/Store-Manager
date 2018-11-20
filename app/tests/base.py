import unittest
from databases.server import DatabaseConnection
from app.utils import bp
from app import app, create_app_environment

app.config.from_object('app.config.ProductionConfig')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app     
        self.app.config['ENV'] = 'testing'   
        self.conn = DatabaseConnection()       
        self.client = self.app.test_client(self)
        self.user = dict(
            username='admin',
            password='testing123'
        )
        self.non_admin = dict(
            username='nonadmin',
            password='testing123'
        )
        self.sale_data = dict(
            product_sold=1,
            quantity=4
        )
        
    
    def tearDown(self):
        self.conn.drop_relation('users')
        self.conn.drop_relation('categories')
        self.conn.drop_relation('products')
        self.conn.drop_relation('sales')
        self.conn.drop_relation('blacklisted')

