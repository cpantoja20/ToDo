from flask import Flask, jsonify, request,json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///example.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.name} {self.content}'

def todo_serializer(todo):
    return {
        'id': todo.id,
        'name': todo.name,
        'content': todo.content
    }   

@app.route('/api', methods = ['GET'])
def index():
    return jsonify([*map(todo_serializer,Todo.query.all())])

@app.route('/api/create', methods = ['POST'])
def create():
    request_data = json.loads(request.data)
    todo = Todo(name = request_data['name'], content = request_data['content'])
    db.session.add(todo)
    db.session.commit()
    return{'201':'To do created succesfully'}

@app.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer,Todo.query.filter_by(id=id))])

@app.route('/api/<int:id>', methods = ['POST'])
def delete(id):
    request_data = json.loads(request.data)
    Todo.query.filter_by(id=request_data['id']).delete()
    db.session.commit()
    return {'204':'To do deleted succesfully'}

if __name__ == '__main__':
    app.run(debug=True)