import unittest
from databases.server import DatabaseConnection
from app import app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.conn = DatabaseConnection()
        self.client = self.app.test_client(self)
        self.user = dict(
            username='soultech',
            password='#phoenix9q'
        )

