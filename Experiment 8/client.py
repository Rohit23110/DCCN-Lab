import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 10000))

message = "I am client\n"
client.send(message.encode('utf-8'))

from_server = client.recv(4096)

client.close()

print(from_server.decode('utf-8'))