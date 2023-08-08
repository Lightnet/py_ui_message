#!/usr/bin/python
from flask import Blueprint, render_template, abort, request
import jwt

from .auth import login_required

bp = Blueprint('simple_page', __name__)

#================================================
# INDEX
#================================================
@bp.route("/")
def index():
  token = request.cookies.get('token')
  if token: #check token exist
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data: #check for sign data
      return render_template('home.html')
  return render_template('index.html')
  #return "Hello"

@bp.route("/test_access")
@login_required
def test_access():
  return "test access"