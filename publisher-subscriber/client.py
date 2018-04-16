import socket
def connection(address, port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((address, int(port)))
    return connection

def send(connection, message):
    connection.send(message)

def sendReceive(connection, message):
    send(connection, message)
    response = connection.recv(64)
    return response