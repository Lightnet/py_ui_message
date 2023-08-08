#!/usr/bin/env python3
# entry point web http server

# https://pypi.org/project/Flask-SocketIO/
# https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
# https://flask-socketio.readthedocs.io/en/latest/getting_started.html
# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
# 

import logging
from flask import Flask
from flask_socketio import SocketIO, emit

from . import database
from .app_module import app
from . import page
from . import auth
from . import database

#app = Flask(__name__)

#================================================
# CONFIG
#================================================
#app.config['SECRET_KEY'] = 'secret!'
#app.config['DEBUG'] = True #auto watch file and reload
#app.config['DATABASE'] = "sqlite.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
#print(app.config)
#socketio = SocketIO(app, logger=False, engineio_logger=False)
#@app.route("/")
#def hello():
  #return "Hello, World!"

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
"""
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
"""
#================================================
# RUN SERVER
#================================================
def create_app():
  #logging.getLogger('socketio').setLevel(logging.ERROR)
  #logging.getLogger('engineio').setLevel(logging.ERROR)
  #app = Flask(__name__)
  #config
  app.config['SECRET_KEY'] = 'secret!'
  app.config['DEBUG'] = True #auto watch file and reload
  app.config['DATABASE'] = "sqlite.db"
  socketio = SocketIO(app, logger=False, engineio_logger=False)

  #blueprint
  app.register_blueprint(auth.bp)
  app.register_blueprint(page.bp)
  app.register_blueprint(database.bp)
  
  # on the local development server.
  #app.run()
  database.init_app(app)

  socketio.run(app, port=3000)
  return app