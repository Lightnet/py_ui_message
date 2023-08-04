#!/usr/bin/python
# built in sqlite3

# https://www.tutorialspoint.com/sqlite/sqlite_python.htm

import sqlite3

def create_table_test(conn):
  conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

def insert_table_test(conn):
  conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

if __name__ == "__main__":
  conn = sqlite3.connect('test.db')
  print("Opened database successfully")

  #create_table_test(conn)
  #print("Table created successfully")
  #insert_table_test(conn)
  #conn.commit()
  
  conn.close() 
  
