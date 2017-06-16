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
global noodlist
global INF
global mainwindow

class DV_main_window(QtWidgets.QMainWindow,DV.Ui_MainWindow):
    def __init__(self):
        super(DV_main_window, self).__init__()
        self.setupUi(self)
        global  noodlist
        noodlist ={}
        global INF
        INF = 99999
        self.setui()
    def setui(self):
        self.addrouterButton.clicked.connect(self.addrouter)
        self.startButton.clicked.connect(self.InitDxy)
    def addrouter(self):
        try:
            routername = self.routername.text()
            text = self.nbnoodinf.text()
            pattern = re.compile(r'(\w:\d)')
            matchs = pattern.findall(text)
            neighbors = {}
            for match in matchs:
                neighbors[match[0]] = match[2]
            nood = Nood(routername,neighbors)
            noodlist[routername] = nood
            routerdate = '添加了节点{},邻居节点有'.format(routername)
            for neighbor in neighbors.keys():
                routerdate = routerdate+'节点{}:距离{};'.format(neighbor,neighbors[neighbor])
            self.routerdate.append(routerdate)
        except:
            self.routerdate.append('输入有误，请重新输入！')
    def InitDxy(self):
        for Nood in noodlist.values():
            for nood in noodlist.values():
                if nood.name in Nood.neighbors:
                    Nood.Dxy[nood.name] = int(Nood.neighbors[nood.name])
                else:
                    Nood.Dxy[nood.name] = INF
            Nood.Dxy[Nood.name] = 0
        for Nood in noodlist.values():
            Nood.Bellman_Ford()
        self.programdate.append('#××××××××××××××××××××××××××#')
        self.programdate.append('#                      更新完毕！                    #')
        self.programdate.append('#××××××××××××××××××××××××××#')
        self.programdate.append('最终结果：')
        for nood in noodlist.values():
            self.programdate.append('节点{}的路由表为：'.format(nood.name))
            str1 = '节点：'
            str2 = '距离：'
            for dxy in nood.Dxy.keys():
                str1 = str1 + '{}  '.format(dxy)
                str2 = str2 + '{}  '.format(nood.Dxy[dxy])
            mainwindow.programdate.append(str1)
            mainwindow.programdate.append(str2)



class Nood(object):
    def __init__(self, routername, neighbors):
        self.name = routername
        self.neighbors = neighbors
        self.Dxy = {}

    def Bellman_Ford(self):
        Dxy_changed = False
        mainwindow.programdate.append('节点{}开始更新'.format(self.name))
        for nood in noodlist.values():
            if self.name == nood.name:
                continue
            Dxy = min(noodlist[neighbor].Dxy[nood.name]
                                          + self.Dxy[neighbor]
                      for neighbor in self.neighbors.keys())
            if self.Dxy[nood.name] != Dxy:
                mainwindow.programdate.append('到节点{}的距离由{}更新至{}'
                                              .format(nood.name,self.Dxy[nood.name],Dxy))
                self.Dxy[nood.name] = Dxy
                Dxy_changed = True
        str1 = '节点：'
        str2 = '距离：'
        for dxy in self.Dxy.keys():
            str1 = str1 + '{}  '.format(dxy)
            str2 = str2 + '{}  '.format(self.Dxy[dxy])
        mainwindow.programdate.append('节点{}的路由表更新后：'.format(self.name))
        mainwindow.programdate.append(str1)
        mainwindow.programdate.append(str2)
        if Dxy_changed:
            for neighbor in self.neighbors.keys():
                noodlist[neighbor].Bellman_Ford()

    # def setneighbor(self, *neighbors):
    #     for neighbor in neighbors:
    #         self.neighbor.add(neighbor)
    #
    # def setnoodlist(self, *noodlist):
    #     for nood in noodlist:
    #         self.noodlist.add(nood)
            # def setCxy(self):
            #     for nood in self.noodlist
            #         if nood is not in self.neighbor:
            #             self.Cxy[nood] = 9999999

            # def initDxy(self):
            #     for nood in self.noodlist:

if __name__ == '__main__':
    # text = '1:2,2:3,3:5,6:9'
    # pattern = re.compile(r'(\w:\d)')
    # matchs = pattern.findall(text)
    # nbnoods = {}
    # for match in matchs:
    #     nbnoods[match[0]] = match[2]
    # sys.setrecursionlimit(1500)  # set the maximum depth as 1500
    global mainwindow
    app = app = QtWidgets.QApplication(sys.argv)
    mainwindow = DV_main_window()
    mainwindow.show()
    sys.exit(app.exec_())