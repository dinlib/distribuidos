from server import create, receive, receiveSend
from client import connection, send, sendReceive
import sys
import argparse

i1port = 1111
i2port = 2222
i3port = 3333

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('subscriber', metavar='N', type=int, nargs=1, help='the subscriber number [1, 2 or 3]')

args = parser.parse_args()
if args.subscriber[0] == 1:
    print 'initializing S1'
elif args.intermed[0] == 2:
    print 'initializing S2' 
elif args.intermed[0] == 3:
    print 'initializing S3'