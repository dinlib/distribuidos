# sudo fuser -k 8091/tcp 8092/tcp 8093/tcp 8094/tcp 8095/tcp 8096/tcp
from server import create, receive, receiveSend
from client import connection, sendmessage, sendReceive
import sys
import argparse
import json
import threading

host = '127.0.0.1'
subPort = 0
subName = ''
subId = ''
i1port = 8091
i2port = 8092
i3port = 8093
s1port = 8094
s2port = 8095
s3port = 8096

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('subscriber', metavar='N', type=int, nargs=1, help='the subscriber number [1, 2 or 3]')

def listenResponse(port):
    serverSocket = create(host, port)
    while 1:
        data = receive(serverSocket)
        dataJSON = json.loads(data)
        print 'Hey, i received the data that i have subscribed from {} {}: {}'.format(dataJSON['name'], dataJSON['id'], dataJSON['data']) 
    


args = parser.parse_args()
if args.subscriber[0] == 1:
    print 'initializing S1'
    subPort = i2port
    subServerPort = s1port
    subName = 'S1'
    subId = '1'
elif args.subscriber[0] == 2:
    print 'initializing S2' 
    subPort = i2port
    subServerPort = s2port
    subName = 'S2'
    subId = '2'
elif args.subscriber[0] == 3:
    print 'initializing S3'
    subPort = i3port
    subServerPort = s3port
    subName = 'S3'
    subId = '3'



t = threading.Thread(target=listenResponse, args=(subServerPort,))
t.start()
while 1:  
    subData = raw_input('What to subscribe with {} ?: '.format(subName))
    # subConnection = connection(host, subPort)
    subJSON = json.dumps({'name':'subscriber', 'id':subId,'data':subData})
    # sendmessage(subConnection, subJSON)
    sendmessage(host, subPort, subJSON)   