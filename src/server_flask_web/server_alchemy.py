# https://pythonbasics.org/#Flask-Tutorial
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# https://devcamp.com/trails/python-api-development-with-flask/campsites/279/guides/creating-sqlite-database-flask-sqlalchemy
# 

from flask import Flask, jsonify, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy
import jwt
from sqlalchemy import func
from .model_alchemy import User, app, db
#import os
#basedir = os.path.abspath(os.path.dirname(__file__))

#================================================
# CONFIG
#================================================
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True #auto watch file and reload

#with app.app_context():
  #print("CREATE DB Table...")
  #db.create_all()
#================================================
# INDEX
#================================================
@app.route("/")
def index():
  
  token = request.cookies.get('token')
  if token: #check token exist
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data: #check for sign data
      return render_template('home.html')
  return render_template('index.html')
  #return "Hello"

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
  print(user)#need to check string
  data ={}
  if userData:
    print("User Exist!")
    print("userData: ", userData)
    print(userData[0].passphrase)
    if userData[0].passphrase == user['passphrase']:
      data['api'] = "PASS"
      token = jwt.encode({"alias": userData[0].alias, 'date':"NOne"}, "secret", algorithm="HS256")

      resp = make_response(jsonify({"alias":user['alias'],"api":"PASS"}))
      resp.set_cookie('token', token)
      return resp
    else:
      data['api'] = "DENIED"
      return jsonify(data)
  else:
    print("FAIL")
    data['api'] = "FAIL"
    return jsonify(data)
  
@app.route('/api/token')
def get_token():
  token = request.cookies.get('token')
  print("token: ", token)
  user_data = jwt.decode(token, "secret", algorithms=["HS256"])
  print("user_data: ", user_data)
  return "token"

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
  #user data
  data = {}
  userData = db.session.execute(db.select(User).filter_by(alias=user['alias'])).fetchone()
  if userData:
    print("User Exist!")
    #print("userData: ", userData)
    #print("userData: ", userData[0].alias)
    #print("userData: ", userData[0].passphrase)
    data['api'] = "EXIST"
  else:
    #CREATE USER
    print("NOT FOUND...")
    new_user = User(
      alias=user['alias'],
      passphrase=user['passphrase']
    )
    db.session.add(new_user) #query
    db.session.commit() #update
    data['api'] = "CREATED"
    
  #data=create_user(user['alias'], user['passphrase'])
  #print("result data: ", data)
  #return jsonify({"msg":"hello"})
  return jsonify(data)

#================================================
# SIGNOUT
#================================================
@app.route('/signout')
def html_signout():
  return render_template('signout.html')

@app.route('/api/signout', methods=['POST'])
def auth_signout():
  #return render_template('index.html')
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      resp = make_response(jsonify({'api':'logout'}))
      resp.set_cookie('token', '', expires=0)
      return resp
    else:
      resp = make_response(jsonify({'api':'NONE'}))
      resp.set_cookie('token', '', expires=0)
  else:
    return jsonify({'api':'NONE'})

@app.route('/admin')
def page_admin():


  return render_template('admin.html')


# Test DB
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
    