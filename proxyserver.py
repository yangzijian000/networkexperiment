#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/6/5 10:42
# @Author : YANGz1J
# @Site : 
# @File : proxyserver.py
# @Software: PyCharm
import socket,threading
import time
class ProxyServer(threading.Thread):
    def __init__(self,cfd,addr):
        threading.Thread.__init__(self)
        self.cfd = cfd
        self.addr = addr
        self.HOST = '127.0.0.1'
        self.PORT = 15123
        self.pfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def run(self):
        print 'Accept from ', self.addr
        msg = self.cfd.recv(1500)
        # print msg
        # pfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.pfd.connect((self.HOST,self.PORT))
        except Exception,e:
            print e
        self.pfd.send(msg)
        while True:
            msg = self.pfd.recv(1500)
            # print msg
            self.cfd.send(msg)
            if not msg:
                break
        self.cfd.close()
        self.pfd.close()
def startserver():
    HOST = ''
    PORT = 15125
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fd.bind((HOST, PORT))
    fd.listen(10)
    print 'Waiting for a client to connect...'
    while True:
        cfd, addr = fd.accept()
        thread = ProxyServer(cfd, addr)
        thread.start()
if __name__ == '__main__':
    startserver()
