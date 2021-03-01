#Todo_app/Api/db/__init__.py

import psycopg2
import SQLqueries as sql

while True:
    try:
        conn = psycopg2.connect(
            database = 'todo',
            user = 'postgres',
            password = 'Nenadb123',
            host='127.0.0.1', 
            port= '5432'
            )
        break
    except:
        conn = psycopg2.connect(
            database="postgres", 
            user='postgres', 
            password='Nenadb123', 
            host='127.0.0.1', 
            port= '5432'
            )
        conn.autocommit = True
        cursor = conn.cursor()
        #Creating a database
        cursor.execute(sql.db_Create)
        conn.close()

def create_tables():
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.tb_create_user)
    cursor.execute(sql.tb_create_task)
    cursor.close()
    conn.close()

# user
def insert_user(name, email, password):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_insert_user, (name, email, password))
    cursor.close()
    conn.close()

def update_user(userId, data, value):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_update_user, (data,value,userId))
    cursor.close()
    conn.close()

def delete_user(userID):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_delete_user, (userId,))
    cursor.close()
    conn.close()

def select_user(userID):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_select_user, (userId,))
    cursor.close()
    conn.close()

# task
def insert_task(name, description, userId):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_insert_task, (name, description, userId))
    cursor.close()
    conn.close()

def update_task(taskId, data, value):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_update_task, (data,value,taskId))
    cursor.close()
    conn.close()

def delete_task(taskId):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_delete_task, (taskId,))
    cursor.close()
    conn.close()

def select_task(taskId):
    conn = psycopg2.connect(database = 'todo',user = 'postgres',password = 'Nenadb123',host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.rw_select_task, (taskId,))
    cursor.close()
    conn.close()


create_tables()
