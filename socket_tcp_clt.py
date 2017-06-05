#!/usr/bin/env python

import socket
import time

HOST = '127.0.0.1'
PORT = 20783
def main():
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        fd.connect((HOST,PORT))
    except Exception as e:
        print (e)
        pass

    msg = input("Type a msg: ")
    fd.send(msg)
    msg = fd.recv(1024)
    print ('\nServer Retrun: \n')
    print (msg)
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("KeyboardInterrupt occurred~~~")
        pass
