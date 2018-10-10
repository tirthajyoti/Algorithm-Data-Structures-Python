# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:55:21 2018

@author: Tirtha
"""

class Node (object):
    def __init__(self,name):
        self.name=name
        
    def getName(self):
        return (self.name)
    
    def __str__(self):
        return (self.name)

class Edge (object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    
    def getSource(self):
        return (self.src)
    
    def getDest(self):
        return (self.dest)
    
    def __str__(self):
        return (self.src+"->"self.dest)
