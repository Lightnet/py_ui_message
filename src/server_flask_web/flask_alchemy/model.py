# app, model and database
# https://www.youtube.com/watch?v=Q2QmST-cSwc
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
# 

# flask and database set up.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
#import os
app = Flask(__name__,template_folder='../templates')

#basedir = os.path.abspath(os.path.dirname(__file__))
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_app.sqlite" #src/instance/project_app.sqlite
#print("BASE: ", os.path.join(basedir, 'app.sqlite'))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

# create the extension
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  alias = db.Column(db.String(32), unique=True, nullable=False)
  passphrase = db.Column(db.String(32), nullable=False)
  email = db.Column(db.String(128))
  role = db.Column(db.String(128), default='member')
  status = db.Column(db.String(128), default='offline')
  created = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
  def __repr__(self):
    return '<User %r>' % self.alias