#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/6/5 11:38
# @Author : YANGz1J
# @Site : 
# @File : UDP_ping_svr.py
# @Software: PyCharm
import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)#建立udp协议的socket连接
serverSocket.bind(('', 12000))
while True:
    rand = random.randint(0, 10)#生成随机数，模拟udp环境下的丢包
    message, address = serverSocket.recvfrom(1024)#接收客户端发送的信息，应该传送ip地址比较好
    message = message.upper()
    if rand < 4: continue#如果随机数字小于4那么就模拟丢包，不进行回复
    serverSocket.sendto(message, address)