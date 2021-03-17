# Api/app.py
from flask import Flask, jsonify, request,json
from blueprints import bp_task

app = Flask(__name__)
app.register_blueprint(bp_task.tasks)

if __name__ == '__main__':
    app.run(debug=True)