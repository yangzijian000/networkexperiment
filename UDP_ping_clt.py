#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/6/5 11:38
# @Author : YANGz1J
# @Site : 
# @File : UDP_ping_clt.py
# @Software: PyCharm
from socket import *
import time

HOST = 'localhost'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # 使用udp协议
clientSocket.bind(('', 6000))  # 绑定端口6000， 也可以不绑定

for i in range(0, 10):  # 发出十次ping
    try:
        start_time = time.time()  # 从发出报文开始计时
        clientSocket.sendto('A', (HOST, PORT))  # 发送报文给服务器
        clientSocket.settimeout(1.0)  # 设置socket等待时间
        message, address = clientSocket.recvfrom(1024)  # recvfrom设置了一秒的时间限制
        end_time = time.time()  # 结束时间
        print "Ping %d %f" % (i, end_time - start_time)  # 得到ttl，并显示出来
    except timeout:  # 如果超过时间，抛出一个timeout的错误
        print "Resquest time out"