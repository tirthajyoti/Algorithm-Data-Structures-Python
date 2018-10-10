# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:21:12 2018
@author: Tirtha
"""

class Stack:
    """
    Stack data structure using list
    """
    def __init__(self,value):
        """
        Class initializer: Produces a stack with a single value or a list of values
        """
        self._items = []
        if type(value)==list:
            for v in value:
                self._items.append(v)
            self._height = len(value)
        else:
            self._items.append(value)
            self._height = 1
        
    def pop(self):
        if self._height == 0:
            print ("Stack is empty. Nothing to pop.")
            return None
        else:
            self._height -=1
            return self._items.pop()
    
    def push(self,value):
        self._height +=1
        self._items.append(value)
        
    def isEmpty(self):
        return self._height==0
    
    def draw(self):
        if self.isEmpty():
            pass
            return None
        else:
            n=self._height
            print('['+str(self._items[n-1])+']')
            for i in range(n-2,-1,-1):
                print(" | ")
                print('['+str(self._items[i])+']')
                    
###==============================================================================================

class Queue:
    """
    Queue data structure using list
    """
    def __init__(self,value):
        """
        Class initializer: Produces a queue with a single value or a list of values
        """
        self._items = []
        if type(value)==list:
            for v in value:
                self._items.append(v)
            self._length = len(value)
        else:
            self._items.append(value)
            self._length = 1
        
    def dequeue(self):
        if self._length == 0:
            print ("Queue is empty. Nothing to dequeue.")
            return None
        else:
            self._length -=1
            return self._items.pop(0)
    
    def enqueue(self,value):
        self._length +=1
        self._items.append(value)
        
    def isEmpty(self):
        return self._length==0
    
    def draw(self):
        if self.isEmpty():
            pass
            return None
        else:
            n=self._length
            for i in range(n-1):
                print('['+str(self._items[i])+']-',end='')
            print('['+str(self._items[n-1])+']')

###=================================================================================

class Tree:
    """
    Recursive definition of Tree class plus various helper functions/methods
    """
    def __init__(self, value, children):
        """
        Class initializer: Produces a single root node having a specific string value; 
        children is a list of references to the root of the children branches.
        Note th children are trees themselves, hence the recursion.
        """
        self._value = value
        self._children = children
        
    def strep(self):
        """
        Generates a string representation of the tree
        """
        text = ""
        text+=str(self._value)
        
        for child in self._children:
            text+='['
            text+=child.strep()
            text+=']'
        return text
    
    def get_value(self):
        return self._value
    
    def children(self):
        for child in self._children:
            yield child
            
    def num_nodes(self):
        result = 1
        for child in self._children:
            result+=child.num_nodes()
        return result
            
    def num_leaves(self):
        if len(self._children)==0:
            return 1
        else:
            result=0
            for child in self._children:
                result += child.num_leaves()
            return result
    
    def height(self):
        height=0
        for child in self._children:
            height = max(height,child.height()+1)
        return height

###================================================================================

class Arithmatic (Tree):
    
    def __init__(self, value, children):
        Tree.__init__(self, value, children)

    def strexp(self):
        if len(self._children)==0:
            return str(self._value)
        else:
            text='('
            text+=self._children[0].strexp()
            text+=str(self._value)
            text+=self._children[1].strexp()
            text+=')'
            return text
    
    def evaluate_exp(self):
        if len(self._children)==0:
            if ('.' in self._value):
                return float(self._value)
            else:
                return int(self._value)
        else:
            function = self._value
            left_value = self._children[0].evaluate_exp()
            right_value = self._children[1].evaluate_exp()
            if function=='+':
                return left_value+right_value
            if function=='-':
                return left_value-right_value
            if function=='*':
                return left_value*right_value
            if function=='/':
                return left_value/right_value
            if function=='%':
                return left_value%right_value
            if function=='^':
                return left_value**right_value