from server import create, receive, receiveSend
from client import connection, send, sendReceive
import sys
import argparse
import json

host = '127.0.0.1'
i1port = 1111
i2port = 2222
i3port = 3333
s1port = 4444
s2port = 5555
s3port = 6666
interId = None

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('intermed', metavar='N', type=int, nargs=1, help='the intermedium number [1, 2 or 3]')

args = parser.parse_args()
ServerSocket = None

intermedList = list();
if args.intermed[0] == 1:
    interId = 1
    print 'initializing i1'
    ServerSocket = create('127.0.0.1', 1111)  
elif args.intermed[0] == 2:
    interId = 2
    print 'initializing i2'
    ServerSocket = create('127.0.0.1', 2222)
elif args.intermed[0] == 3:
    interId = 3
    print 'initializing i3'
    ServerSocket = create('127.0.0.1', 3333)


def seeOnList(dataJSON):
    if len(intermedList) == 0 :
            print 'nothing to be subscribed yet'
        for l in intermedList:
            if(l['data'] == dataJSON['data']):
                if interId == 1:
                    c = connection(host, s2port)
                    c.send(c, dataJSON)
                    c.close()
                elif interId == 2:
                    if l['name'] == 'intermed' and l['id'] == '3':
                        c = connection(host, i3port)
                    elif l['name'] == 'subscriber' and l['id'] == '1':
                        c = connection(host, s1port)
                    elif l['name'] == 'subscriber' and l['id'] == '2':
                        c = connection(host, s2port)
                    send(c, json.dump(dataJSON))
                    c.close            
                elif interId == 3:
                    if l['name'] == 'intermed' and l['id'] == '2':
                        c = connection(host, i2port)
                    elif l['name'] == 'subscriber' and l['id'] == '3':
                        c = connection(host, s3port)
                    send(c, json.dump(dataJSON))
                    c.close
                                       
def spreadTheWord(dataJSON):
    intermedList.append(dataJSON) 

def expressIntention(dataJSON):
    # if interId == 1:
    intermedList.append(dataJSON)                
    if interId == 2:
        dataJSON['name'] = 'intermed'
        dataJSON['id'] = '2'
        newJSON = json.dump(dataJSON)
        c1 = connection(host, i1port)
        c2 = connection(host, i3port)
        c1.send(c1, newJSON)
        c2.send(c2, newJSON)
        c1.close()
        c2.close()
    elif interId == 3:
        dataJSON['name'] = 'intermed'
        dataJSON['id'] = '3'
        newJSON = json.dump(dataJSON)
        c1 = connection(host, i2port)
        c1.send(c1, newJSON)
        c1.close()



while 1:   
    data = receive(ServerSocket)
    dataJSON = json.load(data)
    if dataJSON['name'] == 'publisher':
        seeOnList(dataJSON)
    elif dataJSON['name'] == 'intermed':
        spreadTheWord(dataJSON)
    elif dataJSON['name'] == 'subscriber':
        expressIntention(dataJSON)