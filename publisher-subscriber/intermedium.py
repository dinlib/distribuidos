from server import create, receive, receiveSend
from client import connection, sendmessage, sendReceive
import sys
import argparse
import json
import copy

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
interId = None

parser = argparse.ArgumentParser(description='Create intermediate process')
parser.add_argument('intermed', metavar='N', type=int, nargs=1, help='the intermedium number [1, 2 or 3]')

args = parser.parse_args()
ServerSocket = None


def seeOnList(dataJSON):
    c = None
    if len(intermedList) == 0 :
        print bcolors.Red + 'nothing to be subscribed yet' + bcolors.ENDC
    else:
        count = 0
        for l in intermedList:
            if(l['data'] == dataJSON['data']):
                count += 1
                print bcolors.Yellow + 'Someone has interest on this publication' + bcolors.ENDC
                if interId == 1:
                    print bcolors.White +  'I2 wants the publication... Sending to I2' + bcolors.ENDC
                    sendmessage(host, i2port, json.dumps(dataJSON))
                elif interId == 2:
                    if l['name'] == 'intermed' and l['id'] == '3':
                        print bcolors.White +  'I3 wants the publication... Sending to I3' + bcolors.ENDC
                        sendmessage(host, i3port, json.dumps(dataJSON))
                    elif l['name'] == 'subscriber' and l['id'] == '1':
                        print bcolors.White +  'S1 wants the publication... Sending to S1' + bcolors.ENDC
                        sendmessage(host, s1port, json.dumps(dataJSON))
                    elif l['name'] == 'subscriber' and l['id'] == '2':
                        print bcolors.White +  'S2 wants the publication... Sending to S2' + bcolors.ENDC
                        sendmessage(host, s2port, json.dumps(dataJSON))
                elif interId == 3:
                    if l['name'] == 'intermed' and l['id'] == '2':
                        print bcolors.White +  'I2 wants the publication... Sending to I2' + bcolors.ENDC
                        sendmessage(host, i2port, json.dumps(dataJSON))
                    elif l['name'] == 'subscriber' and l['id'] == '3':
                        print bcolors.White +  'S3 wants the publication... Sending to S3' + bcolors.ENDC
                        sendmessage(host, s3port, json.dumps(dataJSON))
        if count == 0:
            print bcolors.Red + 'No one subscribes this data' + bcolors.ENDC


def spreadTheWord(dataJSON):
    print bcolors.Magenta + 'I{} said that he subscribes {}... updating the route list'.format(dataJSON['id'], dataJSON['data']) + bcolors.ENDC
    intermedList.append(dataJSON) 
    newData = copy.deepcopy(dataJSON)
    if interId == 2:    
        newData['name'] = 'intermed'
        newData['id'] = '2'
        newJSON = json.dumps(newData)
        sendmessage(host, i1port, newJSON)


def expressIntention(dataJSON):
    intermedList.append(dataJSON)
    newData = copy.deepcopy(dataJSON)
    print bcolors.Cyan + 'S{} said that subscribes {}'.format(dataJSON['id'], dataJSON['data']) + bcolors.ENDC               
    if interId == 2:    
        newJSON = json.dumps(newData)
        sendmessage(host, i1port, newJSON)
        sendmessage(host, i3port, newJSON)
    elif interId == 3:
        newData['name'] = 'intermed'
        newData['id'] = '3'
        newJSON = json.dumps(newData)
        sendmessage(host, i2port, newJSON)

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
        print bcolors.Blue + 'Receiving from {} {} the data {}'.format(dataJSON['name'], dataJSON['id'], dataJSON['data']) + bcolors.ENDC
        seeOnList(dataJSON)
    elif dataJSON['name'] == 'intermed':
        print bcolors.Blue + 'Receiving from {} {} the data {}'.format(dataJSON['name'], dataJSON['id'], dataJSON['data']) + bcolors.ENDC
        spreadTheWord(dataJSON)
    elif dataJSON['name'] == 'subscriber':
        print bcolors.Blue + 'Receiving from {} {} the data {}'.format(dataJSON['name'], dataJSON['id'], dataJSON['data']) + bcolors.ENDC
        expressIntention(dataJSON)