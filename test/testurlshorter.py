import unittest
from urlshorter import Urlshorter
from dbcontroller import DB_Controller,MockDbController


class TestUrlShorter(unittest.TestCase):
    urlshorter = None
    mdbcontroller = None
    def setUp(self):
        config = {}
        self.mdbcontroller = MockDbController(config)
        self.urlshorter=Urlshorter(self.mdbcontroller)
        pass
    def test_createUrl(self):
        self.assertEqual(self.urlshorter.create_url('https://google.com'), '05046')
        pass
    def test_getUrl(self):
        pass
    def tearDown(self):
        self.mdbcontroller.close()
        pass