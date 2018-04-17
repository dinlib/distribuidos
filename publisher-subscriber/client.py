import socket
def connection(address, port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((address, int(port)))
    return connection

def sendmessage(address, port, message):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((address, int(port)))
    connection.send(message)

def sendReceive(connection, message):
    sendmessage(connection, message)
    response = connection.recv(64)
    return response