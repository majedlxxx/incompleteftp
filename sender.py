#!/usr/bin/python3
import os
import sys

import socket

def sender(cliaddr,conn,requestedFile):
    f1=open(requestedFile,'r')
    




def client(conn,cliaddr):
    msg="These are the available files enter the number of the file you want to download:\n"
    files=os.listdir('hostedFiles')
    print(files)
    number=0
    for i in files:
        msg=msg+str(number)+": "+i+"\n"
        number+=1
    os.chdir('hostedFiles')
    print(msg)
    conn.send(msg.encode('ascii'))
    requestedFile=conn.recv(4)
    requestedFile=int(requestedFile)
    if requestedFile>=0 and requestedFile<=number:
        print(cliaddr," requested: ",files[requestedFile])
        msg="Getting your file"
        conn.send(msg.encode('ascii'))
    else:
        print(cliaddr," requested invalid file")
        msg="Bad request"
        conn.send(msg.encode('ascii'))
        return
    sender(cliaddr,conn,files[requestedFile])

    return
l=sys.argv
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',5500))
s.listen(10)
while True:
    conn,cliaddr=s.accept()
    print("Got connection from: ", cliaddr)
    client(conn,cliaddr)
    break
