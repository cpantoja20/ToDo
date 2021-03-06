from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.name} {self.content}'