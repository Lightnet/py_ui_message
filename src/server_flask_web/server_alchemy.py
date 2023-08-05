# https://pythonbasics.org/#Flask-Tutorial
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# https://devcamp.com/trails/python-api-development-with-flask/campsites/279/guides/creating-sqlite-database-flask-sqlalchemy
# 

from flask import Flask, jsonify, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from .model_alchemy import User, app, db
#import os
#basedir = os.path.abspath(os.path.dirname(__file__))

#================================================
# CONFIG
#================================================
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True #auto watch file and reload

# create the extension
#db = SQLAlchemy(app)
# initialize the app with the extension
#db.init_app(app)

"""
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  alias = db.Column(db.String, unique=True, nullable=False)
  passphrase = db.Column(db.String, nullable=False)
  email = db.Column(db.String)
  created = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
"""
#with app.app_context():
  #print("CREATE DB Table...")
  #db.create_all()
#================================================
# INDEX
#================================================
@app.route("/")
def index():
  #return "Hello"
  return render_template('index.html')

#================================================
# SIGNIN
#================================================
# Page Html
@app.route('/signin')
def html_sign_in():
  return render_template('signin.html')
# AUTH SIGNIN
@app.route('/api/signin', methods = ['POST'])
def auth_signin():
  user = request.get_json()
  userData = db.session.execute(db.select(User).filter_by(alias=user['alias'])).fetchone()
  if userData:
    print("User Exist!")
    print("userData: ", userData)
  print(user)
  return "Hello"
#================================================
# SIGNUP
#================================================
# Page Html
@app.route('/signup')
def html_signup():
  return render_template('signup.html')

# Auth signup
@app.route('/api/signup', methods = ['POST'])
def auth_signup():
  user = request.get_json()
  #print(user)
  print("ALIAS: ",user['alias'])
  userData = db.session.execute(db.select(User).filter_by(alias=user['alias'])).fetchone()
  if userData:
    print("User Exist!")
    #print("userData: ", userData)
    #print("userData: ", userData[0].alias)
    #print("userData: ", userData[0].passphrase)
  else:
    print("NOT FOUND...")
    new_user = User(
      alias=user['alias'],
      passphrase=user['passphrase']
    )
    db.session.add(new_user) #query
    db.session.commit() #update
    
  #data=create_user(user['alias'], user['passphrase'])
  #print("result data: ", data)
  return jsonify({"msg":"hello"})

#================================================
# SIGNOUT
#================================================
@app.route('/signout')
def html_signout():
  return render_template('signout.html')

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

@app.route('/db_table')
def db_table():
  with app.app_context():
    print("CREATE DB Table...")
    db.create_all()
  db.create_all()
  return ""


#================================================
# INIT SERVER
#================================================
def init_web_server_sql():
  print("init flask sql...")
  # initialize the app with the extension
  #db.init_app(app)
  with app.app_context():
    db.create_all()
  app.run(debug = True, port=3000)
  #pass
    