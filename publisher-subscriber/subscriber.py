from server import create, receive, receiveSend
from client import connection, send, sendReceive
import sys
import argparse

host = '127.0.0.1'
subPort = 0
subName = ''
subId = ''
i1port = 1111
i2port = 2222
i3port = 3333

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('subscriber', metavar='N', type=int, nargs=1, help='the subscriber number [1, 2 or 3]')

args = parser.parse_args()
if args.subscriber[0] == 1:
    print 'initializing S1'
    subPort = i2port
    subName = 'S1'
    subId = '1'
elif args.intermed[0] == 2:
    print 'initializing S2' 
    subPort = i2port
    subName = 'S2'
    subId = '2'
elif args.intermed[0] == 3:
    print 'initializing S3'
    subPort = i3port
    subName = 'S3'
    subId = '3'

while 1:
    subConnection = connection(host, pubPort)
    subData = raw_input('What to subscribe with {} ?: '.format(subName))
    pubJSON = json.dumps('name':'subscriber', 'id':subId,'data':subData)
    response = subConnection.sendReceive(pubConnection, pubJSON)
    print response