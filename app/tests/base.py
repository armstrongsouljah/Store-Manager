import unittest
from databases.server import DatabaseConnection
from app import app, create_app_environment

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.conn = DatabaseConnection()
        self.app.config['ENV'] = 'testing'
        self.client = self.app.test_client(self)
        self.user = dict(
            username='soultech',
            password='#phoenix9q'
        )

