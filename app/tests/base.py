import unittest
from databases.server import DatabaseConnection
from app import create_app_environment

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app_environment('app.config.ProductionConfig')
        self.conn = DatabaseConnection()

