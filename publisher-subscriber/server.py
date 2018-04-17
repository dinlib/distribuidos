import socket

def create(address, port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((address, int(port)))
    serversocket.listen(5) # become a server socket, maximum 5 connections
    print 'Server initialized on {}:{}'.format(address, port)
    return serversocket

def receive(serversocket):
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        # print buf
        return buf

def receiveSend(serversocket, message):
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    # if len(buf) > 0:
        # print buf
    connection.send(message)
        
