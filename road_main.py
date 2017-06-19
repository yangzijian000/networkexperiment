#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/5/21 10:25
# @Author  : YANGz1J
# @Site    : 
# @File    : road_main.py
# @Software: PyCharm
from PyQt5 import QtWidgets
import DV
import re
import sys
global nodelist
global INF
global mainwindow

class DV_main_window(QtWidgets.QMainWindow,DV.Ui_MainWindow):
    def __init__(self):
        super(DV_main_window, self).__init__()
        self.setupUi(self)
        global  nodelist
        nodelist ={}
        global INF
        INF = 99999
        self.setui()
    def setui(self):
        self.addrouterButton.clicked.connect(self.addrouter)
        self.startButton.clicked.connect(self.InitDxy)
        self.updateButton.clicked.connect(self.updaterouter)
    def addrouter(self):
        try:
            routername = self.routername.text()
            text = self.nbnodeinf.text()
            pattern = re.compile(r'(\w+):(\d+)')
            matchs = pattern.findall(text)
            neighbors = {}
            for match in matchs:
                neighbors[match[0]] = match[1]
            node = Node(routername,neighbors)
            nodelist[routername] = node
            routerdate = '添加了节点{},邻居节点有'.format(routername)
            for neighbor in neighbors.keys():
                routerdate = routerdate+'节点{}:距离{};'.format(neighbor,neighbors[neighbor])
            self.routerdate.append(routerdate)
        except:
            self.routerdate.append('输入有误，请重新输入！')
    def InitDxy(self):
        try:
            for Node in nodelist.values():
                for destination in nodelist.values():
                    if destination.name in Node.neighbors:
                        Node.Dxy[destination.name] = int(Node.neighbors[destination.name])
                        Node.nextnodes[destination.name] = destination.name
                    else:
                        Node.Dxy[destination.name] = INF
                        Node.nextnodes[destination.name] = 'No_Path'
                Node.Dxy[Node.name] = 0
                Node.nextnodes[Node.name] = Node.name
            for Node in nodelist.values():
                Node.Bellman_Ford()
            self.programdate.append('#××××××××××××××××××××××××××#')
            self.programdate.append('#                      更新完毕！                    #')
            self.programdate.append('#××××××××××××××××××××××××××#')
            self.programdate.append('最终结果：')
            for Node in nodelist.values():
                self.programdate.append('节点{}的路由表为：'.format(Node.name))
                str1 = '   |'
                str2 = []
                for node in nodelist.values():
                    str1 = str1 + '{} |'.format(node.name)
                    str = '{}  |'.format(node.name)
                    for destination in node.Dxy.keys():
                        str = str + '距离{} 下一跳{} |'.format(node.Dxy[destination], node.nextnodes[destination])
                    str2.append(str)

                mainwindow.programdate.append(str1)
                mainwindow.programdate.append('---|-------------------')
                for str in str2:
                    mainwindow.programdate.append(str)
        except Exception as e:
            print(e)

    def updaterouter(self):
        try:
            routername = self.routername.text()
            text = self.nbnodeinf.text()
            pattern = re.compile(r'(\w+):(\d+)')
            matchs = pattern.findall(text)
            neighbors = {}
            for match in matchs:
                neighbors[match[0]] = match[1]
            nodelist[routername].update(neighbors)
            routerdate = '更新了节点{},邻居节点有'.format(routername)
            for neighbor in neighbors.keys():
                routerdate = routerdate + '节点{}:距离{};'.format(neighbor, neighbors[neighbor])
            self.routerdate.append(routerdate)
        except Exception as e:
            print(e)
class Node(object):
    def __init__(self, routername, neighbors):
        self.name = routername
        self.neighbors = neighbors
        self.Dxy = {}
        self.nextnodes = {}
    def Bellman_Ford(self):
        Dxy_changed = False
        mainwindow.programdate.append('节点{}开始更新'.format(self.name))
        for node in nodelist.values():
            if self.name == node.name:
                continue
            Dxy_all = {}
            for neighbor in self.neighbors.keys():
                Dxy_all[neighbor] = nodelist[neighbor].Dxy[node.name]+ int(self.neighbors[neighbor])
            Dxy = sorted(Dxy_all.items(), key=lambda d: d[1])[0]
            nextnode = Dxy[0]
            if self.Dxy[node.name] != Dxy[1]:
                mainwindow.programdate.append('到节点{}的距离由{}更新至{},下一跳由{}更新至{}'
                                              .format(node.name,self.Dxy[node.name],Dxy[1]
                                                      ,self.nextnodes[node.name],nextnode))
                self.Dxy[node.name] = Dxy[1]
                self.nextnodes[node.name] = nextnode
                Dxy_changed = True
        str1 = '   |'
        str2 = []
        mainwindow.programdate.append('节点{}的路由表更新后：'.format(self.name))
        try:
            for node in nodelist.values():
                str1 = str1 + '{} |'.format(node.name)
                str = '{}  |'.format(node.name)
                for destination in node.Dxy.keys():
                    str = str + '距离{} 下一跳{} |'.format(node.Dxy[destination],node.nextnodes[destination])
                str2.append(str)

            mainwindow.programdate.append(str1)
            mainwindow.programdate.append('---|-------------------')
            for str in str2:
                mainwindow.programdate.append(str)
        except Exception as e:
            print(e)
        if Dxy_changed:
            for neighbor in self.neighbors.keys():
                nodelist[neighbor].Bellman_Ford()

    def update(self,neighbors):
        self.neighbors = neighbors
        self.Bellman_Ford()
if __name__ == '__main__':
    # text = '1:2,2:3,3:5,6:9'
    # pattern = re.compile(r'(\w:\d)')
    # matchs = pattern.findall(text)
    # nbnodes = {}
    # for match in matchs:
    #     nbnodes[match[0]] = match[2]
    # sys.setrecursionlimit(1500)  # set the maximum depth as 1500
    global mainwindow
    app = app = QtWidgets.QApplication(sys.argv)
    mainwindow = DV_main_window()
    mainwindow.show()
    sys.exit(app.exec_())