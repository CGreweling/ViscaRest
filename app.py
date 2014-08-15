import os
from flask import Flask, request
from flask.ext.restful import Resource, Api
from flask.ext import restful

app = Flask(__name__)
api = Api(app)

todos = {}
viscaCommand= "./visca_cli -d /dev/ttyUSB0 "

class TodoSimple(Resource):
    def get(self, todo):
        return {todo: todos[todo]}

    def put(self, todo):
        todos[todo] = request.form['data']
        viscaCommand="./visca_cli -d /dev/ttyUSB0 "+todos[todo]
        print viscaCommand
        os.system(viscaCommand)
        return {todo: todos[todo]}

class Index(restful.Resource):
   def get(self):
        text='Bedienung mit Rest: curl http://localhost:5000/viscaDo/pan -d "data=set_pantilt_relative_position 10 10 10 10" -X PUT'	
        return text 

api.add_resource(TodoSimple, '/viscaDo/<string:todo>')
api.add_resource(Index,'/')

if __name__ == '__main__':
    app.run(debug=True)
