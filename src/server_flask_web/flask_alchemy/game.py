# https://flask.palletsprojects.com/en/2.3.x/tutorial/views/

from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
import jwt

from .model import User, db

#bp = Blueprint('auth', __name__, url_prefix='/auth')
bp = Blueprint('game', __name__)
#================================================
# Game
#================================================
@bp.route('/game/control')
def page_admin():
  token = request.cookies.get('token')
  if token:
    user_data = jwt.decode(token, "secret", algorithms=["HS256"])
    if user_data:
      print("FOUND TOKEN:", request.cookies.get('token'))
      #resp = make_response(jsonify({'api':'logout'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp

    else:
      #resp = make_response(jsonify({'api':'NONE'}))
      #resp.set_cookie('token', '', expires=0)
      #return resp
      return render_template('game.html')
  else:
    #return jsonify({'api':'NONE'})
    return render_template('game.html')
  return render_template('game.html')