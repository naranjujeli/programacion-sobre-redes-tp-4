import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Cambia la dirección y el puerto según tus necesidades
client_socket.connect(server_address)

# Prepara datos JSON
data = {'nombre': 'Ejemplo', 'edad': 25}
json_data = json.dumps(data)

# Envía datos JSON al servidor
client_socket.send(json_data.encode())

# Recibe una respuesta del servidor
response_data = client_socket.recv(1024).decode()
response_json = json.loads(response_data)

# Procesa la respuesta del servidor
print("Respuesta del servidor:")
print(response_json)

# Cierra la conexión
client_socket.close()