from server import create, receive, receiveSend
from client import connection, sendmessage, sendReceive
import sys
import argparse
import json
class bcolors:
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

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
    pubData = raw_input(bcolors.BOLD + 'What to pub with {} ?: '.format(pubName) + bcolors.ENDC)
    pubJSON = json.dumps({'name':'publisher', 'id':pubId,'data':pubData})
    sendmessage(host, pubPort, pubJSON)
    print 'Publishing with {} the data {}'.format(pubName, pubData)



