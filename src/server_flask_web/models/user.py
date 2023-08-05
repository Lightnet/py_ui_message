# https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
# https://therenegadecoder.com/code/how-to-convert-sqlite3-rows-into-python-objects/
# 

import sqlite3
import jwt
from server_flask_web.database import get_db

def create_user(_name, _pass):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE alias = ?',(_name,))
    checkUsername = cursor.fetchone()
    print("checkUsername: ", checkUsername)
    if checkUsername:
        print('Logged In!')
        user : list[sqlite3.Row] = checkUsername

        #print(user)
        print(user['alias'])
        #print(checkUsername)
        #print(checkUsername[0])
        #print(checkUsername[1])
        #print(checkUsername[2])
        #print(checkUsername['username'])
    else:
        print('Username does not exist')
        cursor.execute('INSERT INTO user (alias, passphrase) VALUES(?, ?)', (_name, _pass) )
        conn.commit()

    conn.close()

def login_check_user(_name, _pass):
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM user WHERE alias = ?',(_name,))
  checkUsername = cursor.fetchone()
  print("checkUsername: ", checkUsername)
  data = {}
  if checkUsername:
    print('Logged In!')
    user : list[sqlite3.Row] = checkUsername

    #print(user)
    print(user['alias'])
    #print(checkUsername)
    #print(checkUsername[0])
    #print(checkUsername[1])
    #print(checkUsername[2])
    #print(checkUsername['username'])
    token = jwt.encode({"alias": "test"}, "secret", algorithm="HS256")
    print("token: ", token)
    data['token'] = token
    data['api'] = "PASS"
  else:
    print('Username does not exist')
    data['api'] = "FAIL"

  conn.close()
  return data

"""
def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["name"] = i["name"]
            user["email"] = i["email"]
            user["phone"] = i["phone"]
            user["address"] = i["address"]
            user["country"] = i["country"]
            users.append(user)
    except:
        users = []
    return users

def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", 
                       (user_id,))
        row = cur.fetchone()
        # convert row object to dictionary
        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["email"] = row["email"]
        user["phone"] = row["phone"]
        user["address"] = row["address"]
        user["country"] = row["country"]
    except:
        user = {}
    return user

def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?",  
                     (user["name"], user["email"], user["phone"], 
                     user["address"], user["country"], 
                     user["user_id"],))
        conn.commit()
        #return the user
        updated_user = get_user_by_id(user["user_id"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user
"""