import unittest

from dbcontroller import MockDbController

class TestDbController(unittest.TestCase):
    dbcontroller = None
    def setUp(self):
        config = {}
        self.dbcontroller = MockDbController(config)

    def test_geturl(self):
        self.assertEqual(self.dbcontroller.geturl(b'foo'), b'bar')

    def test_saveurl(self):
        self.assertEqual(self.dbcontroller.saveurl(b'foo', b'bar'), b'foo')

    def tearDown(self):
        self.dbcontroller.close()
