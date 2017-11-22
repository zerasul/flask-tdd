'''
dbcontroller: control the actions with the database controller
'''
class DB_Controller:
    def __init__(self,config):
        pass
    def saveurl(self, code, url):
        pass
    def geturl(self, code):
        pass
    def close(self):
        pass

class MockDbController(DB_Controller):
    def __init__(self, config):
        pass
    def geturl(self, code):
        if code == b'foo':
            return b'bar'
        elif code == b'google.com':
            return b'bar2'
    def saveurl(self, code, url):
       return code