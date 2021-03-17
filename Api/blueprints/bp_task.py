# Api/blueprints/bp_task.py

import sys
sys.path.append("..")
from flask import Blueprint, jsonify, request, json
from db import db

tasks = Blueprint('task', __name__)

def todo_serializer(task):
    return {
        'id': task[0],
        'name': task[1],
        'content': task[2]
    }   

@tasks.route('/api', methods = ['GET'])
def index():
    return jsonify([*map(todo_serializer,db.select_all_task())])

@tasks.route('/api/create', methods = ['POST'])
def create():
    request_data = json.loads(request.data)
    db.insert_task(request_data['name'], request_data['content'])
    return{'201':'To do created succesfully'}

@tasks.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer,db.select_task(id))])

@tasks.route('/api/<int:id>', methods = ['POST'])
def delete(id):
    request_data = json.loads(request.data)
    db.delete_task(str(id))
    return {'204':'To do deleted succesfully'}