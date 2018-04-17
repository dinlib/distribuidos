from server import create, receive, receiveSend
from client import connection, sendmessage, sendReceive
import sys
import argparse
import json
import copy

host = '127.0.0.1'
i1port = 8091
i2port = 8092
i3port = 8093
s1port = 8094
s2port = 8095
s3port = 8096
interId = None

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('intermed', metavar='N', type=int, nargs=1, help='the intermedium number [1, 2 or 3]')

args = parser.parse_args()
ServerSocket = None


def seeOnList(dataJSON):
    c = None
    if len(intermedList) == 0 :
        print 'nothing to be subscribed yet'
    else:
        print '------seeOnList------'
        print intermedList
        for l in intermedList:
            if(l['data'] == dataJSON['data']):
                print 'Someone has interest on this publication'
                if interId == 1:
                    print 'I2 wants the publication... Sending to I2'
                    # c = connection(host, s2port)
                    # sendmessage(c, json.dumps(dataJSON))
                    sendmessage(host, i2port, json.dumps(dataJSON))
                    # c.close()
                elif interId == 2:
                    if l['name'] == 'intermed' and l['id'] == '3':
                        print 'I3 wants the publication... Sending to I3'
                        # c = connection(host, i3port)
                        sendmessage(host, i3port, json.dumps(dataJSON))
                    elif l['name'] == 'subscriber' and l['id'] == '1':
                        print 'S1 wants the publication... Sending to S1'
                        # c = connection(host, s1port)
                        sendmessage(host, s1port, json.dumps(dataJSON))
                    elif l['name'] == 'subscriber' and l['id'] == '2':
                        print 'S2 wants the publication... Sending to S2'
                        # c = connection(host, s2port)
                        sendmessage(host, s2port, json.dumps(dataJSON))
                    # sendmessage(c, json.dumps(dataJSON))
                    # c.close            
                elif interId == 3:
                    if l['name'] == 'intermed' and l['id'] == '2':
                        print 'I2 wants the publication... Sending to I2'
                        # c = connection(host, i2port)
                        sendmessage(host, i2port, json.dumps(dataJSON))
                    elif l['name'] == 'subscriber' and l['id'] == '3':
                        print 'S3 wants the publication... Sending to S3'
                        # c = connection(host, s3port)
                        sendmessage(host, s3port, json.dumps(dataJSON))
                    # c.close


def spreadTheWord(dataJSON):
    print '------spreadTheWord------'
    print intermedList
    print 'I{} said that he subscribes {}... updating the route list'.format(dataJSON['id'], dataJSON['data'])
    intermedList.append(dataJSON) 
    newData = copy.deepcopy(dataJSON)
    if interId == 2:    
        newData['name'] = 'intermed'
        newData['id'] = '2'
        newJSON = json.dumps(newData)
        # c1 = connection(host, i1port)
        sendmessage(host, i1port, newJSON)
        # c1.close()


def expressIntention(dataJSON):
    # if interId == 1:
    print '------expressIntention------'
    print intermedList
    intermedList.append(dataJSON)
    newData = copy.deepcopy(dataJSON)
    print 'S{} said that subscribes {}'.format(dataJSON['id'], dataJSON['data'])                
    if interId == 2:    
        newData['name'] = 'intermed'
        newData['id'] = '2'
        newJSON = json.dumps(newData)
        # c1 = connection(host, i1port)
        # c2 = connection(host, i3port)
        sendmessage(host, i1port, newJSON)
        sendmessage(host, i3port, newJSON)
        # c1.close()
        # c2.close()
    elif interId == 3:
        newData['name'] = 'intermed'
        newData['id'] = '3'
        newJSON = json.dumps(newData)
        # c1 = connection(host, i2port)
        sendmessage(host, i2port, newJSON)
        # c1.close()


intermedList = list()
if args.intermed[0] == 1:
    interId = 1
    print 'initializing i1'
    ServerSocket = create(host, i1port)  
elif args.intermed[0] == 2:
    interId = 2
    print 'initializing i2'
    ServerSocket = create(host, i2port)
elif args.intermed[0] == 3:
    interId = 3
    print 'initializing i3'
    ServerSocket = create(host, i3port)

while 1:   
    data = receive(ServerSocket)
    dataJSON = json.loads(data)
    if dataJSON['name'] == 'publisher':
        print 'Receiving from {} {} the data {}'.format(dataJSON['name'], dataJSON['id'], dataJSON)
        seeOnList(dataJSON)
    elif dataJSON['name'] == 'intermed':
        print 'Receiving from {} {} the data {}'.format(dataJSON['name'], dataJSON['id'], dataJSON)
        spreadTheWord(dataJSON)
    elif dataJSON['name'] == 'subscriber':
        print 'Receiving from {} {} the data {}'.format(dataJSON['name'], dataJSON['id'], dataJSON)
        expressIntention(dataJSON)