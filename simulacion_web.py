from simulation import Simulation
from cronopio import ParserCronopio
import socket as sk
import json

class SimulacionWeb(Simulation):

    def __init__(self, **kargs):
        super().__init__(**kargs)


    def simulate(self, generation):
        
        parser = ParserCronopio()
        dicts = [parser.from_cronopio_to_json(cronopio) for cronopio in generation]
        json_data = json.dumps(dicts)   

        #ACA MANDARIAMOS POR SOKETS EL JSON
        #Y GUARDARIAMOS LOS CRONOPIOS DE RESPUESTA EN UNA VARIABLE LLAMADABA dead_cronopios
        dead_cronopios = []


        result = [parser.from_json_to_cronopio(cronopio_json) for cronopio_json in dead_cronopios]
        return result
    
def mandar_por_socket(paquete):

    server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Esperando una conexion")
    client_socket, client_address = server_socket.accept()
    print(f"Conexion establecida con {client_address}")

    data = client_socket.recv(1024).decode()
    received_data = json.loads(data)

    print("Datos recibidos: ")
    print(received_data)

    response_data = {"respueta": "Datos recibidos con exito"}
    response_json = json.dumps(response_data)
    client_socket.send(response_json.encode())

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":

    mandar_por_socket("nashe")