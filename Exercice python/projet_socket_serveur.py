# serveur

import socket


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print('attente de connection sur {HOST_IP}, port {HOST_PORT}')
connect, client= s.accept()
print(f"connexion établie avec {client}")