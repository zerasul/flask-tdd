import hashlib
from dbcontroller import DB_Controller
'''
 class URLShorter: this class generate a shorter url or get the complete url from the code.
 '''
class Urlshorter:
    dbcontroller  = None
    def __init__(self,dbcontroller):
        self.dbcontroller=dbcontroller
        pass
    def create_url(self, url):
        code = self.__create_code(url)
        return self.dbcontroller.saveurl(code, url)
        
    def get_url(self, code):
        return self.dbcontroller.geturl(code)
        pass
    def __create_code(self, url):
        mhash = hashlib.sha256(url.encode('utf-8')).hexdigest()
        return mhash[:5]
pass
