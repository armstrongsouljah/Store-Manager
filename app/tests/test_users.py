import unittest

from app.models.users import User

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.obj = User(1,'soultech', True, 'password')

    def test_instantiation(self):
        self.assertIsInstance(self.obj, User)