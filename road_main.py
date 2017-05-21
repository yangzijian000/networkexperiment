#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/5/21 10:25
# @Author  : YANGz1J
# @Site    : 
# @File    : road_main.py
# @Software: PyCharm
class nood(object):
    def __init__(self):
        self.noodlist = set()
        self.neighbor = set()
        self.Cxy = {}
        self.Dxy = {}
    def setneighbor(self,*neighbors):
        for neighbor in neighbors:
            self.neighbor.add(neighbor)

    def setnoodlist(self,*noodlist):
        for nood in noodlist:
            self.noodlist.add(nood)
    def setCxy(self):
        for nood in self.noodlist
            if nood is not in self.neighbor:
                self.Cxy[nood] = 9999999

    def initDxy(self):
        for nood in self.noodlist:
            self.Dxy[nood] = min()



