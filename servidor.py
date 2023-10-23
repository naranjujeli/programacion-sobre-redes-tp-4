from flask import Flask
from flask_socketio import SocketIO, send

# Crear una instancia de Socket.IO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on("connection")
async def connection(socket):
    socket.send("hola", "hola")
    

if __name__ == '__main__':
    app.run(debug=True)