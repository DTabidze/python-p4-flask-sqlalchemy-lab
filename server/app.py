#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Zoo app</h1>"


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    response = ""
    animal_id = animal.id
    name = animal.name
    species = animal.species
    zookeeper = animal.zookeeper
    enclosure = animal.enclosure
    response += f"<ul>ID: {animal_id}</ul>"
    response += f"<ul>Name: {name}</ul>"
    response += f"<ul>Species: {species}</ul>"
    response += f"<ul>Zookeeper: {zookeeper.name}</ul>"
    response += f"<ul>Enclosure: {enclosure.environment}</ul>"
    return response


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    response = ""
    zookeeper_id = zookeeper.id
    name = zookeeper.name
    birthday = zookeeper.birthday
    response += f"<ul>ID: {zookeeper_id}</ul>"
    response += f"<ul>Name: {name}</ul>"
    response += f"<ul>Birthday: {birthday}</ul>"
    for animal in zookeeper.animals:
        # animals = zookeeper.animals[1]
        # print(animal.name)
        response += f"<ul>Animal: {animal.name}</ul>"
    # print(animals)
    return response


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    enclosure_id = enclosure.id
    environment = enclosure.environment
    open_to_visitors = enclosure.open_to_visitors
    response = ""
    response += f"<ul>ID: {enclosure_id}</ul>"
    response += f"<ul>Environment: {environment}</ul>"
    response += f"<ul>Open to Visitors: {open_to_visitors}</ul>"
    for animal in enclosure.animals:
        # animals = zookeeper.animals[1]
        # print(animal.name)
        response += f"<ul>Animal: {animal.name}</ul>"
    # print(animals)
    return response
    return ""


if __name__ == "__main__":
    app.run(port=5555, debug=True)
