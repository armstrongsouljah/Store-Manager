from .base import BaseTestCase


class TestDatbaseOperations(BaseTestCase):
    def test_connection_working(self):
        self.assertTrue(self.conn)