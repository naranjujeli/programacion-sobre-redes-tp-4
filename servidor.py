from aiohttp import web
import socketio

# Crear una instancia de Socket.IO
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.on("connection")
async def connection():
    print("SE PRENDIO ESTA MIERDA")

if __name__ == '__main__':
    web.run_app(app)

# Definir una función que se ejecutará cuando un cliente se conecte
# @sio.event
# def connect(sid, environ):
#     print(f"Cliente conectado: {sid}")

# # Definir una función para recibir y enviar mensajes
# @sio.event
# def message(sid, data):
#     print(f"Mensaje recibido de {sid}: {data}")
#     # Puedes procesar el mensaje recibido y enviar una respuesta si es necesario
#     response = {'message': 'Respuesta del servidor'}
#     sio.emit('response', response, room=sid)

# # Definir una función que se ejecutará cuando un cliente se desconecte
# @sio.event
# def disconnect(sid):
#     print(f"Cliente desconectado: {sid}")

