from .base import BaseTestCase


class TestDatabaseOperations(BaseTestCase):

    def test_database_connected(self):
        self.assertTrue(self.conn)