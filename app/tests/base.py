import unittest
from app import app
from app.database.server import DatabaseConnection



class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = DatabaseConnection()   