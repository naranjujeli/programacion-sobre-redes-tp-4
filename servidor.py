from flask import Flask
from flask_socketio import SocketIO
from simulacion_web import SimulacionWeb
from cronopio import ParserCronopio

# Crear una instancia de Socket.IO

app = Flask(__name__)
server = SocketIO(app, cors_allowed_origins='*')

width = 750
height = 400
food = 500
generation_size = 21
frame = 15
reproduction_pool_size = 7
mutation_parameters = 0.4

parser = ParserCronopio()
simulation = None

@server.event
async def connect(sock): 
    socket = sock
    simulation = SimulacionWeb(socket = socket, width=width, height=height, food=food, generation_size=generation_size, frame=frame, reproduction_pool_size=reproduction_pool_size, mutation_parameters=mutation_parameters)

@server.event
async def dead_gen(data):
    dead_cronopios = [parser.from_json_to_cronopio(cronopio_json) for cronopio_json in data["cronopios"]]
    simulation.client.emit("new_gen", simulation.generate(dead_cronopios))

# @socketio.on("json")
# def a(data):
#     print(data)

if __name__ == '__main__':
    app.run(debug=True)