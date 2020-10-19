import time
from flask import Flask,request
from datetime import datetime
app = Flask(__name__)

messages = [
    {'username': 'Saveli', 'time': time.time(), 'text': 'Hello!'},
    {'username': 'Alina', 'time': time.time(), 'text': 'Hello, Savli!'}
]

password_storage = {
    'Saveli': '159753258',
    'Alina': '4815162342'
}

@app.route("/status")
def statusMethod():
    return{
        'status': True,
        'datetime': datetime.now()
    }


@app.route("/")
def helloMethod():
    return "Hello world!"

@app.route("/send", methods=['POST'])
def sendMethod():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']


    if username not in password_storage:
        password_storage[username] = password

    if not isinstance(username, str) or len(username) == 0:
        return{"loh":False}
    if not isinstance(text, str) or len(text) == 0:
        return{"loh":False}
    if password_storage[username] != password:
        return{'Vzlom jopi ne proizashel))':False}

    messages.append({'username':username,'time':time.time(), 'text':text})

    return{'ok':True}

@app.route("/messages")
def messagesMethod():

    after = float(request.args['after'])
    filtered_messages = [message for message in messages if message['time'] > after]


    return{'messages':filtered_messages}

app.run()
