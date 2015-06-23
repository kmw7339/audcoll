#!/usr/bin/python

from flask import Flask, request
from flask_restful import Resource, Api

class AudCollApi():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)        
        self.api.add_resource(EcaStatus,'/EcaStatus')
        self.api.add_resource(SetName,'/SetName/<string:ecaname>', endpoint="ecaname")

    def run(self):
        self.app.run(debug=True)

class SetName(Resource):
    def get(self,ecaname):
        return { 'SetName': ecaname }

class EcaStatus(Resource):
    def get(self):
        return { 'EcaStatus': 'OK' }



if __name__ == '__main__':
    aci = AudCollApi()
    aci.run()
