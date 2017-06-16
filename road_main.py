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
            for destination in noodlist.values():
                if destination.name in Nood.neighbors:
                    Nood.Dxy[destination.name] = int(Nood.neighbors[destination.name])
                    Nood.nextnoods[destination.name] = destination.name
                else:
                    Nood.Dxy[destination.name] = INF
                    Nood.nextnoods[destination.name] = 'No_Path'
            Nood.Dxy[Nood.name] = 0
            Nood.nextnoods[Nood.name] = Nood.name
        for Nood in noodlist.values():
            Nood.Bellman_Ford()
        self.programdate.append('#××××××××××××××××××××××××××#')
        self.programdate.append('#                      更新完毕！                    #')
        self.programdate.append('#××××××××××××××××××××××××××#')
        self.programdate.append('最终结果：')
        try:
            for Nood in noodlist.values():
                self.programdate.append('节点{}的路由表为：'.format(Nood.name))
                str1 = '   |'
                str2 = []
                for nood in noodlist.values():
                    str1 = str1 + '{} |'.format(nood.name)
                    str = '{}  |'.format(nood.name)
                    for destination in nood.Dxy.keys():
                        str = str + '距离{} 下一跳{} |'.format(nood.Dxy[destination], nood.nextnoods[destination])
                    str2.append(str)

                mainwindow.programdate.append(str1)
                mainwindow.programdate.append('---|-------------------')
                for str in str2:
                    mainwindow.programdate.append(str)
        except Exception as e:
            print(e)



class Nood(object):
    def __init__(self, routername, neighbors):
        self.name = routername
        self.neighbors = neighbors
        self.Dxy = {}
        self.nextnoods = {}
    def Bellman_Ford(self):
        Dxy_changed = False
        mainwindow.programdate.append('节点{}开始更新'.format(self.name))
        for nood in noodlist.values():
            if self.name == nood.name:
                continue
            Dxy_all = {}
            for neighbor in self.neighbors.keys():
                Dxy_all[neighbor] = noodlist[neighbor].Dxy[nood.name]+ self.Dxy[neighbor]
            Dxy = sorted(Dxy_all.items(), key=lambda d: d[1])[0]
            nextnood = Dxy[0]
            if self.Dxy[nood.name] != Dxy[1]:
                mainwindow.programdate.append('到节点{}的距离由{}更新至{},下一跳由{}更新至{}'
                                              .format(nood.name,self.Dxy[nood.name],Dxy[1]
                                                      ,self.nextnoods[nood.name],nextnood))
                self.Dxy[nood.name] = Dxy[1]
                self.nextnoods[nood.name] = nextnood
                Dxy_changed = True
        str1 = '   |'
        str2 = []
        mainwindow.programdate.append('节点{}的路由表更新后：'.format(self.name))
        try:
            for nood in noodlist.values():
                str1 = str1 + '{} |'.format(nood.name)
                str = '{}  |'.format(nood.name)
                for destination in nood.Dxy.keys():
                    str = str + '距离{} 下一跳{} |'.format(nood.Dxy[destination],nood.nextnoods[destination])
                str2.append(str)

            mainwindow.programdate.append(str1)
            mainwindow.programdate.append('---|-------------------')
            for str in str2:
                mainwindow.programdate.append(str)
        except Exception as e:
            print(e)
        if Dxy_changed:
            for neighbor in self.neighbors.keys():
                noodlist[neighbor].Bellman_Ford()

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