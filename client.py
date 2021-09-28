"""
        Programmer : Trevor Avila
        Program Description: Client and server program using Transmission Control Protocol and IPv4
        Date : 9/24/21
        Last Changed: 9/28/21
"""
# library
import socket

# creating the client socket
client = socket.socket()

# connecting to the server with given ip and port number
client.connect(('localhost', 9999))

# user input for the host name
name = input("enter your host name")

client.send(bytes(name, 'utf-8')) # sending the data to server

print(client.recv(1024).decode())  # receiving the data from server
