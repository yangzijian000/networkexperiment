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

class Nood(object):
    def __init__(self, routername, neighbors):
        self.name = routername
        self.neighbors = neighbors
        self.Dxy = {}

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


class DV_main_window(QtWidgets.QMainWindow,DV.Ui_MainWindow):
    def __init__(self):
        super(DV_main_window, self).__init__()
        self.setupUi(self)
        self.noodlist =[]
        global INF
        INF = 99999
        self.setui()
    def setui(self):
        self.addrouterButton.clicked.connect(self.addrouter)

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
            self.noodlist.append(nood)
            routerdate = '添加了节点{},邻居节点有'.format(routername)
            for neighbor in neighbors.keys():
                routerdate = routerdate+'节点{}:距离{};'.format(neighbor,neighbors[neighbor])
            self.routerdate.append(routerdate)
        except:
            self.routerdate.append('输入有误，请重新输入！')
    def InitDxy(self):
        for Nood in self.noodlist:
            for nood in self.noodlist:
                if Nood.neighbors.has_key(nood.name):
                    Nood.Dxy[nood.name] = Nood.neighbors[nood.name]
                else:
                    Nood.Dxy[nood.name] = INF





if __name__ == '__main__':
    # text = '1:2,2:3,3:5,6:9'
    # pattern = re.compile(r'(\w:\d)')
    # matchs = pattern.findall(text)
    # nbnoods = {}
    # for match in matchs:
    #     nbnoods[match[0]] = match[2]
    app = app = QtWidgets.QApplication(sys.argv)
    mainwindow = DV_main_window()
    mainwindow.show()
    sys.exit(app.exec_())