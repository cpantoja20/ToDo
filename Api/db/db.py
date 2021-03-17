#Api/db/db.py

import psycopg2

db_config = {'database': 'todo', 'user': 'postgres',
                     'password': 'Nenadb123', 'host': '127.0.0.1', 'port': '5432'}

while True:
    try:
        conn = psycopg2.connect(**db_config)
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
        cursor.execute('''CREATE database ToDo''')
        conn.close()

def create_tables():
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks(
        id serial NOT NULL PRIMARY KEY,
        name CHAR(20) NOT NULL,
        description VARCHAR(255) NOT NULL
        )''')
    cursor.close()
    conn.close()

# task
def insert_task(name, description):
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Tasks (id, name, description) VALUES (DEFAULT,%s,%s)''', (name, description))
    cursor.close()
    conn.close()

def delete_task(taskId):
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM Tasks WHERE id = %s""", (str(taskId)))
    cursor.close()
    conn.close()

def select_task(taskId):
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Tasks WHERE id = %s""", (str(taskId)))
    task = cursor.fetchall()
    cursor.close()
    conn.close()
    return task

def select_all_task():
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Tasks""")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

create_tables()

