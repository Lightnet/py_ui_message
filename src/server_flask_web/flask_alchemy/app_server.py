# https://pythonbasics.org/#Flask-Tutorial
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# https://devcamp.com/trails/python-api-development-with-flask/campsites/279/guides/creating-sqlite-database-flask-sqlalchemy
# https://flask.palletsprojects.com/en/2.3.x/blueprints/#why-blueprints

#import os
from .model import app, db

from . import auth
from . import admin
from . import game
from . import url_page

#================================================
# CONFIG
#================================================
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SECRET_KEY'] = 'secret!'
#app.config['DEBUG'] = True #auto watch file and reload
#app.register_blueprint(auth_alchemy.bp)

#================================================
# CONFIG
#================================================
def create_app():
  #config
  app.config['SECRET_KEY'] = 'secret!'
  app.config['DEBUG'] = True #auto watch file and reload

  #blueprint
  app.register_blueprint(url_page.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(admin.bp)
  app.register_blueprint(game.bp)

  #init datbase by cmd line ''
  with app.app_context():
    db.create_all()
  app.run(debug = True, port=3000)
  return app