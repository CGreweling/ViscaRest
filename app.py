import os
from flask import Flask, request, render_template
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
        text='Bedienung mit Rest und curl: curl http://localhost:5000/curlDo/pan -d "data=set_pantilt_relative_position 10 10 10 10" -X PUT'	
        return text 


@app.route('/post', methods = ['GET','POST'])
def getPersonById():	
    if request.method == 'POST':
       return 'POST'
    if request.method == 'GET':
        command = request.args.get('todo', '')
        viscaCommand="./visca_cli -d /dev/ttyUSB0 "+command
        print viscaCommand
        os.system(viscaCommand)
        return viscaCommand   
    return 'no Method'

@app.route('/')
def message():
    return render_template('index.html')


api.add_resource(TodoSimple, '/curlDo/<string:todo>')
api.add_resource(Index,'/curlDo')

if __name__ == '__main__':
    app.debug= True
    app.run(host='0.0.0.0')
