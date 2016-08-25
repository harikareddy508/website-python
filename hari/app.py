#!/usr/bin/env python

#standard libraries
from datetime import datetime
from flask import Flask, request, send_from_directory, jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

#utility functions
from constants import Methods
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app)


"""
    SQlAlchemy magic happening here. I am using this library to map objects to sql and vice versa
"""


class Person(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    department = db.Column(db.String(100))
    person = db.Column(db.String(100))
    description = db.Column(db.String(100))

    def __init__(self, json):
        self.department = json['department']
        self.person = json['person']
        self.description = json['description']

    def serialize(self):
        return {'id': self.id,
                'department': self.department,
                'person': self.person,
                'description': self.description
                }


"""
    Method called for /. We check whether we are getting any query params as part of request, if we get any we will send
    json if not we render index.html
"""


@app.route('/')
def index():
    # checking whether we are getting query params as part of request
    if len(request.args) > 0:
        search_string = '%'+str(request.args['search'])+'%';
        persons = Person.query.filter(Person.department.like(search_string) | Person.description.like(search_string) | Person.person.like(search_string)).all()
        return jsonify(persons=[person.serialize() for person in persons])
    else:
        return render_template('index.html')


"""
    Method which will be triggered for form submission
"""


@app.route('/', methods=[Methods.POST])
def add_person():
    # checking whether we are submitting empty form
    if len(request.json) > 0:
        person = Person(request.json)
        db.session.add(person)
        db.session.commit()
        return jsonify(persons={})
    else:
        return render_template('index.html')


"""
    Method which will serve JS files located in css directory using send_from_directory
"""


@app.route('/js/<path>')
def send_js(path):
    return send_from_directory('js', path)


"""
    Method which will serve CSS files located in css directory using send_from_directory
"""


@app.route('/css/<path>')
def send_css(path):
    return send_from_directory('css', path)


if __name__ == '__main__':
    app.run()
