# Api/db/queries.py

# Database

db_Create = '''CREATE database ToDo'''

#Tables

     #Task

tb_create_task ='''CREATE TABLE IF NOT EXISTS Tasks(
    id serial NOT NULL PRIMARY KEY,
    name CHAR(20) NOT NULL,
    description VARCHAR(255) NOT NULL,
    )'''

#CRUD

    #Task

select_all_tasks ="""SELECT * FROM Tasks"""

rw_insert_task = '''INSERT INTO Tasks (id, name, description, user_id) VALUES (DEFAULT,%s,%s,%s)'''

rw_select_task = """SELECT * FROM Tasks WHERE id = %s"""

rw_update_task = """UPDATE Tasks SET %s = %s where id = %s"""

rw_delete_task = """DELETE FROM Tasks WHERE id = %s"""
