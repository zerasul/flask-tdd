'''
flaskapp: aplicacion web que tiene la siguiente configuracion
/ -> GET muestra una web con un formulario
/<codigo> -> GET realiza una redireccion hacia la url guardada; si no existe devolvera un 404
/ -> POST guarda una nueva url.
'''
from flask import request, Flask, render_template, redirect
from urlshorter import Urlshorter
from dbcontroller import MockDbController

app = Flask(__name__,template_folder='templates')
app.debug=1
class webHandler:
    config = app.config
    DbController = MockDbController(config)
    urlShorter = Urlshorter(DbController)
    def getIndex(self):
        return render_template('index.html')
        pass
    def post_url(self, url):
        code = self.urlShorter.create_url(url)
        return render_template('index.html', url=code)
        pass
    def get_url(self, code):
        return redirect('https://google.com')
        pass


webHandler = webHandler()
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return webHandler.getIndex()
    elif request.method == 'POST':
        return webHandler.post_url(request.form['url'])

    pass
@app.route('/<code>', methods=['GET'])
def geturl(code):
    return webHandler.get_url(code)
    pass