#Todo_app/Api/db/SQLQueries.py

# Database

db_Create = '''CREATE database ToDo'''

#Tables

    #User

tb_create_user ='''CREATE TABLE IF NOT EXISTS Users(
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY(ID)
    )'''

     #Task

tb_create_task ='''CREATE TABLE IF NOT EXISTS Tasks(
    id INT NOT NULL,
    name CHAR(20) NOT NULL,
    description VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
    )'''

#CRUD

    #User

rw_insert_user = '''INSERT INTO Users (name, email, password) VALUES (%s,%s,%s)'''

rw_select_user = """SELECT * FROM Users WHERE id = %s"""

rw_update_user = """UPDATE Users SET %s = %s where id = %s"""

rw_delete_user = """DELETE FROM Users WHERE id = %s"""

    #Task

        #Insert

rw_insert_task = '''INSERT INTO Users (name, description, user_id) VALUES (%s,%s,%s)'''

rw_select_task = """SELECT * FROM Users WHERE id = %s"""

rw_update_task = """UPDATE Users SET %s = %s where id = %s"""

rw_delete_task = """DELETE FROM Users WHERE id = %s"""