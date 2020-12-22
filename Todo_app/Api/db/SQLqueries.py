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
    status BOOL,
    PRIMARY KEY(ID)
    )'''

     #Task

tb_create_task ='''CREATE TABLE IF NOT EXISTS Tasks(
    id INT NOT NULL,
    name CHAR(20) NOT NULL,
    description VARCHAR(255) NOT NULL,
    status BOOL,
    user_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
    )'''