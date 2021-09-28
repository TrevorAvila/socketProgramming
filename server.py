"""
        Programmer : Trevor Avila
        Program Description: Client and server program using Transmission Control Protocol and IPv4
        Date : 9/24/21
        Last Changed: 9/28/21
"""

#library
import socket

# using default par (ipv4, TCP)
server = socket.socket()
print("Server socket created")

# binding ipaddress and port
server.bind(('localhost', 9999))

# server is going to connect with 3 clients at a given time
server.listen(3)
print("server waiting for connections")

while True:
    client, ipaddress = server.accept() # retrieving client and its ip
    name = client.recv(1024).decode() # receiving data to client
    print("server is now connected with ", ipaddress, name) # showing connection with the name and ip variable names
    client.send(bytes("you're now connected with the server", 'utf-8')) # sending the data to client
    client.close()  # closing the connection