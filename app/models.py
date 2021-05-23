from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prioritize.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<ID: {}, Name: {}>'.format(self.id, self.name)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    task = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text(), nullable=True)
    imp = db.Column(db.Boolean, default=False, nullable=False)
    urg = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<ID: {}, Task: {}>'.format(self.id, self.task)