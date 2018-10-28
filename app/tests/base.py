import unittest
from databases.server import DatabaseConnection
from app import app, create_app_environment

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
    
    def tearDown(self):
        self.conn.drop_relation('users')

