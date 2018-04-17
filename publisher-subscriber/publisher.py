from server import create, receive, receiveSend
from client import connection, sendmessage, sendReceive
import sys
import argparse
import json

host = '127.0.0.1'
i1port = 8091
i2port = 8092
i3port = 8093
s1port = 8094
s2port = 8095
s3port = 8096
pubId = ''
pubName = ''
pubPort = 0

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('publisher', metavar='N', type=int, nargs=1, help='the publisher number [1 or 2]')

args = parser.parse_args()
if args.publisher[0] == 1:
    print 'initializing P1'
    pubName = 'P1'
    pubId = '1'
    pubPort = i1port  
elif args.publisher[0] == 2:
    print 'initializing P2'
    pubName = 'P2'
    pubId = '2'
    pubPort = i3port 

while 1:
    pubData = raw_input('What to pub with {} ?: '.format(pubName))
    # pubConnection = connection(host, pubPort)
    pubJSON = json.dumps({'name':'publisher', 'id':pubId,'data':pubData})
    # response = sendReceive(pubConnection, pubJSON)
    sendmessage(host, pubPort, pubJSON)
    print 'Publishing with {} the data {}'.format(pubName, pubJSON)
    # print response


