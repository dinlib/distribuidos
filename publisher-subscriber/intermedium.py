from server import create, receive, receiveSend
from client import connection, send, sendReceive
import sys
import argparse
import json

host = '127.0.0.1'
i1port = 1111
i2port = 2222
i3port = 3333
a1port = 4444
a2port = 5555
a3port = 6666

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('intermed', metavar='N', type=int, nargs=1, help='the intermedium number [1, 2 or 3]')

args = parser.parse_args()
ServerSocket = None

intermedList = list();
if args.intermed[0] == 1:
    print 'initializing i1'
    ServerSocket = create('127.0.0.1', 1111)  
elif args.intermed[0] == 2:
    print 'initializing i2'
    ServerSocket = create('127.0.0.1', 2222)
elif args.intermed[0] == 3:
    print 'initializing i3'
    ServerSocket = create('127.0.0.1', 3333)

while 1:   
    data = receive(ServerSocket)
    dataJSON = json.load(data)
    if dataJSON['name'] == 'P1':
        if(len(intermedList) == 0):
            print 'nothing to be subscribed yet'
        for l in intermedList:
            if(l['data'] == dataJSON['data']):
                c = connection(host, i2port)
                c.send(c, dataJSON)
    elif dataJSON['name'] == 'P2': 
        if(len(intermedList) == 0):
            print 'nothing to be subscribed yet'
        for l in intermedList:
            if(l['data'] == dataJSON['data']):
                c = connection(host, a3port)
                c.send(c, dataJSON) 
    elif dataJSON['name'] == 'I1' or dataJSON['name'] == 'I2' or dataJSON['name'] == 'I3':
    
    elif dataJSON['name'] == 'S1' or dataJSON['name'] == 'S2' or dataJSON['name'] == 'S3':
