# https://pypi.org/project/Flask-SocketIO/
# https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
# https://flask-socketio.readthedocs.io/en/latest/getting_started.html
# 


from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#@app.route("/")
#def hello():
  #return "Hello, World!"

@app.route('/')
def index():
  return render_template('index.html')

@socketio.event
def my_event(message):
  emit('my response', {'data': 'got it!'})

@socketio.on('message')
def handle_message(data):
  print('received message: ' + data)

@socketio.on('connect')
def connect():
  print("client connected")
  #if not self.authenticate(request.args):
    #raise ConnectionRefusedError('unauthorized!')

def init_web_server():
  # run() method of Flask class runs the application
  # on the local development server.
  #app.run()
  socketio.run(app)