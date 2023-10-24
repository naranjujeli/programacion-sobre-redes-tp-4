from flask import Flask
from flask_socketio import SocketIO, send

# Crear una instancia de Socket.IO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.event
def connect(sid):
    print("CONNECTION ESTABLISHED")
    socketio.emit("hello", { "hola": "hola" }, to=sid)

@socketio.event
def hello(data):
    print("HELLO RECEIVED")
    print(data)
    return data["hola"]

# @socketio.on("json")
# def a(data):
#     print(data)

if __name__ == '__main__':
    app.run(debug=True)