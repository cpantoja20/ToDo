# Api/app.py
from flask import Flask, jsonify, request,json
from flask_sqlalchemy import SQLAlchemy
from db import db

app = Flask(__name__)

def todo_serializer(task):
    return {
        'id': task[0],
        'name': task[1],
        'content': task[2]
    }   

@app.route('/api', methods = ['GET'])
def index():
    return jsonify([*map(todo_serializer,db.select_all_task())])

@app.route('/api/create', methods = ['POST'])
def create():
    request_data = json.loads(request.data)
    db.insert_task(request_data['name'], request_data['content'])
    return{'201':'To do created succesfully'}

@app.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer,db.select_task(id))])

@app.route('/api/<int:id>', methods = ['POST'])
def delete(id):
    request_data = json.loads(request.data)
    db.delete_task(id)
    return {'204':'To do deleted succesfully'}

if __name__ == '__main__':
    app.run(debug=True)