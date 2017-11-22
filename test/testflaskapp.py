import unittest
import server

class TestServer(unittest.TestCase):

    def setUp(self):
        server.app.testing=1
        self.app = server.app.test_client()
    
    def testIndex(self):
        assert b'Bienvenidos a Flask' in self.app.get('/').data
        pass
    def testPostUrl(self):
        data=dict(url='https://google.com')
        assert b'05046' in self.app.post('/', data = data).data
        pass

if __name__ == '__main__':
    unittest.main()
    