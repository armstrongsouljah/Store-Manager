from .base import BaseTestCase


class TestDatbaseOperations(BaseTestCase):
    def test_connection_working(self):
        self.assertTrue('connection successful', self.conn)