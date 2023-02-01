import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import Any

# get the base dir
basedir = os.path.abspath(os.path.dirname(__file__))

# create the app
app = Flask(__name__)

# configure the PostgreSQL database
#app.config["SQLALCHEMY_DATABASE_URI"] = \
#    "postgresql://postgres:unlockdb@localhost:5432/bajaj"

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'pets.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the extension
db: SQLAlchemy = SQLAlchemy(app)
app.app_context().push()
Migrate(app, db)

class Pet(db.Model):
    __tablename__: str = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    toys = db.relationship('Toy', backref='pets', lazy='dynamic')
    owner = db.relationship('Owner', backref='pets', uselist=False)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return f'Pet\'s name is { self.name } and owner is { self.owner.name }'

    def report_toys(self) -> None:
        print('There are many toys')
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    __tablename__: str = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def __init__(self, item_name: str, pet_id: int) -> None:
        super().__init__()
        self.item_name = item_name
        self.pet_id = pet_id

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def __init__(self, name: str, pet_id: int) -> None:
        super().__init__()
        self.name = name
        self.pet_id = pet_id