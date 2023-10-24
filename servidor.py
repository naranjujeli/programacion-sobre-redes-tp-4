from flask import Flask
from flask_socketio import SocketIO, send
from simulacion_web import SimulacionWeb
from cronopio import ParserCronopio

# Crear una instancia de Socket.IO

app = Flask(__name__)
server = SocketIO(app, cors_allowed_origins='*')

class Server:

    def __init__(self): 

        self.__width = 750
        self.__height = 400
        self.__food = 500
        self.__generation_size = 21
        self.__frame = 15
        self.__reproduction_pool_size = 7
        self.__mutation_parameters = 0.4

        self.__parser = ParserCronopio()



    @server.event
    def connect(self, sock): 
        self.__socket = sock
        self.__simulation = SimulacionWeb(socket = self.__socket, width=self.__width, height=self.__height, food=self.__food, generation_size=self.__generation_size, frame=self.__frame, reproduction_pool_size=self.__reproduction_pool_size, mutation_parameters=self.__mutation_parameters)
        

    @server.event
    def dead_gen(self, data):
        dead_cronopios = [self.__parser.from_json_to_cronopio(cronopio_json) for cronopio_json in data["cronopios"]]
        self.__simulation.client.emit("new_gen", self.__simulation.generate(dead_cronopios))

# @socketio.on("json")
# def a(data):
#     print(data)

if __name__ == '__main__':
    app.run(debug=True)