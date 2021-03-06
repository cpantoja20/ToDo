from flask import Flask, jsonify
from Api.models import db
from Api.blueprints import todos

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///example.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(todos)

if __name__ == '__main__':
    app.run(debug=True)
