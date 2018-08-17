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
        return (self.src.getName()+"->"+self.dest.getName())
    
class Digraph(object):
    def __init__(self):
        self.edges={}
        
    def addNode(self,node):
        if node in self.edges:
            raise ValueError("Duplicate node")
        else:
            self.edges[node]=[]
    
    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDest()
        if (src not in self.edges) and (dest not in self.edges):
            raise ValueError("Node not in graph")
        else:
            self.edges[src].append(dest) # Builds adjacency list
    
    def childrenOf(self,node):
        return self.edges[node]
    
    def hasNode(self,node):
        return node in self.edges
    
    def getNode(self,name):
        for n in self.edges:
            if n.getName()==name:
                return n
            raise NameError(name)
    
    def __str__(self):
        toPrint=''
        for src in self.edges:
            for dest in self.edges[src]:
                toPrint=toPrint+src.getName()+"->"+dest.getName()+"\n"
                    
        if (toPrint==''):
            return ("Empty graph! Nothing to print")
        else:
            return toPrint[:-1]
    
