# https://flask.palletsprojects.com/en/2.3.x/tutorial/views/

from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
import jwt

from .model import User, db

#bp = Blueprint('auth', __name__, url_prefix='/auth')
bp = Blueprint('admin', __name__)
#================================================
# ADMIN
#================================================
@bp.route('/admin/control')
def page_admin():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/admin.html')
    
  return render_template('admin/admin.html')

@bp.route('/admin/groupmessages')
def page_admin_groupmessages():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/groupmessages.html')
    
  return render_template('admin/admin.html')

@bp.route('/admin/reports')
def page_admin_reports():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/reports.html')
    
  return render_template('admin/admin.html')

@bp.route('/admin/members')
def page_admin_members():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #users = db.session.execute(db.select(User).filter_by()).fetchall()
      users= User.query.all()
      
      print("userDatas: ", users)
      print(users)

      return render_template('admin/members.html',members=users)
    
  return render_template('admin/admin.html')

@bp.route('/admin/permissions')
def page_admin_permissions():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/permissions.html')
    
  return render_template('admin/admin.html')

@bp.route('/admin/groups')
def page_admin_groups():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/groups.html')
    
  return render_template('admin/admin.html')

@bp.route('/admin/bans')
def page_admin_bans():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/bans.html')
    
  return render_template('admin/admin.html')

@bp.route('/admin/settings')
def page_admin_settings():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('admin/settings.html')
    
  return render_template('admin/admin.html')

#need to pending for register amdin or mod
@bp.route('/admin/signup')
def auth_admin_signup():
  token = request.cookies.get('token')
  return render_template('admin/admin.html')

@bp.route('/admin/sigin')
def auth_admin_signin():
  token = request.cookies.get('token')
  return render_template('admin/admin.html')

@bp.route('/admin/signout')
def auth_admin_signout():
  token = request.cookies.get('token')
  return render_template('admin/admin.html')