# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:41:33 2017

@author: Mekii
"""

import socket,threading
import time
#import sys



#from datetime import datetime
contentTypeLine="Content-type:"
class sevrthread(threading.Thread):
    def __init__(self,sfd,addr):
        threading.Thread.__init__(self)
        self.sfd=sfd
        self.addr=addr
    def run(self):
        print 'Accept from ', self.addr
        msg = self.sfd.recv(1500)

        try:
            filename = msg.decode('utf-8').split(' ')[1]
            print msg
            print filename
            x=open('.'+filename,"rb").read()
            self.sfd.send(bytearray("HTTP/1.1 200 OK"+"\r\n",'utf8'))  
            self.sfd.send(bytearray("Content-type:"+self.webtype(filename)+"\r\n",'utf8'))
            self.sfd.send(bytearray("Date:"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\r\n",'utf8'))  
            self.sfd.send(bytearray("\r\n",'utf8'))  
            self.sfd.send(x)
            self.sfd.close()
        except:
            self.sfd.send(bytearray("HTTP/1.1 404 NotFound"+"\r\n",'utf8'))
            self.sfd.send(bytearray("Content-type:text/html"+"\r\n",'utf8'))
            self.sfd.send(bytearray("Date:"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\r\n"))
            self.sfd.send(bytearray("\r\n",'utf8'))  
            self.sfd.send(bytes("<h1>404</h1>"))
            self.sfd.close()
            #pagesrc = '<html><body><h1>Hello Word %s</h1></body></html>' % datetime.strftime(datetime.today(), '%Y-%m-%d %H:%M:%S')
            #httpmsg = 'HTTP/1.1 200 OK\r\nDate: Sat, 31 Dec 2017 23:59:59 GMT\r\nContent-Type: '+webtype(url)+'; charset=utf-8\r\nContent-Length: %d\r\n\r\n%s' % (len(pagesrc), msg)
            #sfd.send(httpmsg)                

    def webtype(self,filename):
        filetype=filename.split('.')[1]
        if filetype=='text':
            return 'text/html'
        if filetype=='jpg':
            return 'image/jpeg'           
if __name__ == '__main__':
    HOST = ''
    PORT = 15123
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fd.bind((HOST, PORT))
    fd.listen(10)
    print 'Waiting for a client to connect...'
    while True:
        sfd, addr = fd.accept()
        thread=sevrthread(sfd,addr)
        thread.start()