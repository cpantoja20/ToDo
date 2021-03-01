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

conn.autocommit = True

def create_tables():
    cursor = conn.cursor()
    cursor.execute(sql.tb_create_user)
    cursor.execute(sql.tb_create_task)
    conn.close()


create_tables()