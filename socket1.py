import socket  # Imports the socket library

# Make a socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to a destination across the internet
mySocket.connect(('data.pr4e.org', 80))
# Send an HTTP command to the server
# http://data.pr4e.org/intro-short.txt
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mySocket.send(command)

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mySocket.close()
