#!/usr/bin/env python3

# Tests
# entry point web http server

# https://pypi.org/project/Flask-SocketIO/
# https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
# https://flask-socketio.readthedocs.io/en/latest/getting_started.html
# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
# 

import logging
from flask import Flask, jsonify, make_response, render_template, request
from flask_socketio import SocketIO, emit

from server_flask_web.flask_sqlite import db_sqlite
from server_flask_web.flask_sqlite.user_sqlite import create_user, login_check_user

app = Flask(__name__)

#================================================
# CONFIG
#================================================
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True #auto watch file and reload
app.config['DATABASE'] = "sqlite.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
#print(app.config)
socketio = SocketIO(app, logger=False, engineio_logger=False)
#@app.route("/")
#def hello():
  #return "Hello, World!"
#================================================
# INDEX
#================================================
@app.route('/')
def index():
  #request
  token = request.cookies.get('token')
  print("token: ", token)
  if token:
    return render_template('home.html')
  else:
    return render_template('index.html')
  
#================================================
# SIGNIN
#================================================
# Page render
@app.route('/signin')
def html_sign_in():
  return render_template('signin.html')
# https://www.geeksforgeeks.org/flask-cookies/
# Auth login
@app.route('/api/signin', methods = ['POST'])
def auth_signin():
  user = request.get_json()
  print(user)
  #name = request.cookies.get('userID')
  data = login_check_user(user['alias'],user['passphrase'])
  print("result data: ", data)
  if data['api'] == "PASS":
    print("PASS TOKEN...")
    resp = make_response(jsonify({"alias":user['alias']}))
    resp.set_cookie('token', data['token'])
    return resp
    #pass
  else:
    return jsonify({"api":"FAIL"})
  #resp = make_response(jsonify({"hello":"world"}))
  #resp.set_cookie('somecookiename', 'I am cookie')
  #return resp 
  #return render_template('index.html')
  #return jsonify(insert_user(user))
#================================================
# SIGNUP
#================================================
# page render
@app.route('/signup')
def url_signup():
  return render_template('signup.html')

# Auth signup
@app.route('/api/signup', methods = ['POST'])
def auth_signup():
  #user = request.get_json()
  #user = request.get_data()
  user = request.get_json()
  
  print(user)
  data=create_user(user['alias'], user['passphrase'])
  print("result data: ", data)

  #user = request.form.get('alias')
  #passphrase = request.form.get('passphrase')
  #user = request.get_data(parse_form_data=True)
  #print(user)
  #print(passphrase)
  #return render_template('index.html')
  return jsonify({"msg":"hello"})
#================================================
# SIGNOUT
#================================================
@app.route('/signout')
def page_signout():
  return render_template('signout.html')
  #return jsonify([u.to_json() for u in users])

@app.route('/api/signout', methods=['POST'])
def auth_signout():
  #return render_template('index.html')
  if request.cookies.get('token'):
    print("FOUND TOKEN:", request.cookies.get('token'))
    resp = make_response(jsonify({'api':'logout'}))
    resp.set_cookie('token', '', expires=0)
    return resp
  else:
    return jsonify({'api':'NONE'})


#================================================
# SOCKET.IO
#================================================
#@socketio.event
#def my_event(message):
  #emit('my response', {'data': 'got it!'})

#@socketio.on('message')
#def handle_message(data):
  #print('received message: ' + data)

#@socketio.on('connect')
#def connect():
  #print("client connected")
  #if not self.authenticate(request.args):
    #raise ConnectionRefusedError('unauthorized!')
#================================================
# DATABASE
#================================================
@app.route('/db')
def check_db():
  mydb = db_sqlite.get_db()
  print(mydb)
  return "Hello DB!"
  #return render_template('index.html')

@app.route('/db_createtable')
def db_create_table():
  db_sqlite.init_db()
  return "DB TABLE!"
  #return render_template('index.html')
#================================================
# RUN SERVER
#================================================
def init_web_server():
  logging.getLogger('socketio').setLevel(logging.ERROR)
  logging.getLogger('engineio').setLevel(logging.ERROR)
  # run() method of Flask class runs the application
  # on the local development server.
  #app.run()
  db_sqlite.init_app(app)

  socketio.run(app, port=3000)