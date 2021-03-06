from flask import Blueprint, jsonify, request
from Api.models import Todo, db
from Api.utils import todo_serializer

todos = Blueprint('todos', __name__)


@todos.route('/api', methods = ['GET'])
def index():
    return jsonify([*map(todo_serializer,Todo.query.all())])

@todos.route('/api/create', methods = ['POST'])
def create():
    request_data = json.loads(request.data)
    todo = Todo(name = request_data['name'], content = request_data['content'])
    db.session.add(todo)
    db.session.commit()
    return{'201':'To do created succesfully'}

@todos.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer,Todo.query.filter_by(id=id))])

@todos.route('/api/<int:id>', methods = ['POST'])
def delete(id):
    request_data = json.loads(request.data)
    Todo.query.filter_by(id=request_data['id']).delete()
    db.session.commit()
    return {'204':'To do deleted succesfully'}