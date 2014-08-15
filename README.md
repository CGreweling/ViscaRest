ViscaRest
=========

Control libVisca over Python REST

Download install libvisca
copy /libvisca/example/visca_cli* into the app.py folder

sudo apt-get install python-virtualenv
pip install flask
flask/bin/pip install flask-restful

set your rs232 visca connector in app.py

falsk/bin/python2.7 app.py
http://yourip:5000 shows a little help

Example how it works:
curl http://localhost:5000/viscaDo/pan -d "data=set_pantilt_relative_position 10 10 200 200" -X PUT
