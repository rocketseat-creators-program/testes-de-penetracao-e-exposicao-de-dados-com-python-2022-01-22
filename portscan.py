import socket
import sys

portas = [80,21,22,443]
url = sys.argv[1]

for porta in portas:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.1)
        codigo = cliente.connect_ex((url,int(porta)))
        if codigo == 0:
                print porta, "OPEN"
