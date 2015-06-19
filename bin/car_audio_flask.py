#!/usr/bin/python

from flask import Flask, request
from flask_restful import Resource, Api

class AudCollApi():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)        
        self.api.add_resource(TodoSimple,'/<string:todo_id>')

    def run(self):
        self.app.run(debug=True)

class TodoSimple(Resource):
    def __init__(self):
        self.todos = {}

    def get(self, todo_id):
        return {todo_id: self.todos[todo_id]}

    def put(self, todo_id):
        self.todos[todo_id] = request.form['data']
        return {todo_id: self.todos[todo_id]}

if __name__ == '__main__':
    aci = AudCollApi()
    aci.run()
