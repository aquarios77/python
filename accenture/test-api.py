# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:37:16 2021

@author: antons.sincovs
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)