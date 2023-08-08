#!/usr/bin/python
"""
  Auth access for sign up, in, and out for account build access
"""

import functools
from flask import Blueprint, jsonify, make_response, render_template, request
from server_flask_web.flask_sqlite.user_sqlite import create_user, login_check_user

#bp = Blueprint('auth', __name__, url_prefix='/auth')
bp = Blueprint('auth', __name__)

#================================================
# SIGNIN
#================================================
# Page render
@bp.route('/signin')
def html_sign_in():
  return render_template('signin.html')
# https://www.geeksforgeeks.org/flask-cookies/
# Auth login
@bp.route('/api/signin', methods = ['POST'])
def auth_signin():
  user = request.get_json()
  #print(user)
  #name = request.cookies.get('userID')
  data = login_check_user(user['alias'],user['passphrase'])
  #print("result data: ", data)
  if data['api'] == "PASS":
    #print("PASS TOKEN...")
    resp = make_response(jsonify({"alias":user['alias'], "api":"PASS"}))
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
@bp.route('/signup')
def url_signup():
  return render_template('signup.html')

# Auth signup
@bp.route('/api/signup', methods = ['POST'])
def auth_signup():
  #user = request.get_json()
  #user = request.get_data()
  user = request.get_json()
  user['alias']
  if not user['alias'] or not user['passphrase']:
    return jsonify({"api":"EMPTY"}) 
  print(user)
  data=create_user(user['alias'], user['passphrase'])
  print("result data: ", data)
  if data:
    return jsonify({"api":data['api']})  
  else:
    return jsonify({"api":"ERROR"})  

  #user = request.form.get('alias')
  #passphrase = request.form.get('passphrase')
  #user = request.get_data(parse_form_data=True)
  #print(user)
  #print(passphrase)
  #return render_template('index.html')
  #return jsonify({"msg":"hello"})
#================================================
# SIGNOUT
#================================================
@bp.route('/signout')
def page_signout():
  return render_template('signout.html')
  #return jsonify([u.to_json() for u in users])

@bp.route('/api/signout', methods=['POST'])
def auth_signout():
  #return render_template('index.html')
  if request.cookies.get('token'):
    print("FOUND TOKEN:", request.cookies.get('token'))
    resp = make_response(jsonify({'api':'logout'}))
    resp.set_cookie('token', '', expires=0)
    return resp
  else:
    return jsonify({'api':'NONE'})

def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    print("CHECK LOGIN REQUIRED")
    print(g)
    #if g.user is None:
      
      #return redirect(url_for('/login'))
      ##return redirect(url_for('auth.login'))

    return view(**kwargs)

  return wrapped_view