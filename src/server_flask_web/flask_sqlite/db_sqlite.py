#!/usr/bin/python
# https://pynative.com/python-sqlite/
# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
# https://flask.palletsprojects.com/en/2.3.x/tutorial/database/
# https://stackoverflow.com/questions/51822129/access-flask-app-context-in-cli-command



import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
  if 'db' not in g:
    print("init db: ",current_app.config['DATABASE'])
    g.db = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row

  return g.db

def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()

def init_db():
  db = get_db()
  print("init db")
  with current_app.open_resource('../schemas/user.sql') as f:
    print("init start table")
    db.executescript(f.read().decode('utf8'))

# https://flask.palletsprojects.com/en/2.3.x/tutorial/database/
# cmd line py server.py init-db
@click.command('init-db')
@with_appcontext
def init_db_command():
  print("CMD INIT DATABASE CREATE TABLE")
  """Clear the existing data and create new tables."""
  init_db()
  click.echo('Initialized the database.')

def init_app(app):
  #print("init database...")
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)

# Test DB
"""
@app.route('/db_table')
def db_table():
  with app.app_context():
    print("CREATE DB Table...")
    db.create_all()
  db.create_all()
  return ""

try:
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
  cursor.close()

except sqlite3.Error as error:
  print("Error while connecting to sqlite", error)
finally:
  if conn:
    conn.close()
    print("The SQLite connection is closed")

def connect_to_db():
  conn = sqlite3.connect('sqlite.db')
  #conn.row_factory = sqlite3.Row
  return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        conn.close()
"""