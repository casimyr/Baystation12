#!/usr/bin/env python2

# Two arguments, channel and message.
# EG: "ircbot_message.py #adminchannel ADMINHELP, people are killing me!"

import sys,cPickle,socket

def pack():
    passwd = sys.argv[1]
    ip = sys.argv[3]
    try:
        data = sys.argv[4:] #The rest of the arguments is data
    except:
        data = "NO DATA SPECIFIED"
    dictionary = {"ip":ip,"data":[passwd] + data}
    pickled = cPickle.dumps(dictionary)
    nudge(pickled)
def nudge(data):
    HOST = sys.argv[2]
    PORT = 45678
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.send(data)
    s.close()

if __name__ == "__main__" and len(sys.argv) > 1: # If not imported and more than one argument
    pack()
