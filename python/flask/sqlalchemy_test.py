from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "postgresql://postgres:unlockdb@localhost:5432/bajaj"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    
class Student(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)