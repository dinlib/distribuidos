from server import create, receive, receiveSend
from client import connection, send, sendReceive
import sys
import argparse
import json

host = '127.0.0.1'
i1port = 1111
i2port = 2222
i3port = 3333
pubName = ''
pubPort = 0

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('publisher', metavar='N', type=int, nargs=1, help='the publisher number [1 or 2]')

args = parser.parse_args()
if args.publisher[0] == 1:
    print 'initializing P1'
    pubName = 'P1'
    pubPort = i1port  
elif args.publisher[0] == 2:
    print 'initializing P2'
    pubName = 'P2'
    pubPort = i2port 

while 1:
    pubConnection = connection(host, pubPort)
    pubData = raw_input('What to pub with {} ?: '.format(pubName))
    pubJSON = json.dumps('name':pubName, 'data':pubData)
    response = pubConnection.sendReceive(pubConnection, pubJSON)
    print response


