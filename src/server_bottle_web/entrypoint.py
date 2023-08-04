
# https://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world
from bottle import route, run, template, get, post, request, static_file, error

@route('/hello/<name>')
def index(name):
  return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def hello():
  return "Hello World!"

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(_name,_pass):

  return True

@route('/static/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root='/path/to/your/static/files')

#@error(404)
#def error404(error):
  #return 'Nothing here, sorry'

@route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = wsock.receive()
            wsock.send("Your message was: %r" % message)
        except WebSocketError:
            break

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

def init_web_server():
  run(host='localhost', port=8080)