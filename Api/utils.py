from flask import jsonify

def todo_serializer(todo):
    return {
        'id': todo.id,
        'name': todo.name,
        'content': todo.content
    }