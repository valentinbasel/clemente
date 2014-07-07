# !/usr/bin/python           # This is client.py file

import socket               # Import socket module
import time
s = socket.socket()         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 9999                # Reserve a port for your service.

s.connect((host, port))

for a in range(10000):
    #~ print a
    s.send("analogico,1")
    peticion = s.recv(1024)
    print peticion
    #~ time.sleep(0.5)
s.send("cerrar")

s.close                     # Close the socket when done
