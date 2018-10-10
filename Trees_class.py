# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:00:12 2018

@author: Tirtha
"""

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
    

tree_a = Tree('a',[])
tree_b = Tree('b',[])

tree_cab = Tree('c',[tree_a,tree_b])

print (tree_a.strep())
print(tree_b.get_value())
print(tree_cab.strep())

tree_4 = Tree('d',[tree_cab,tree_b,tree_a])
print (tree_4.strep())
print(tree_4.num_nodes())
print(tree_4.num_leaves())
print(tree_4.height())


OPERATORS = {
             "+":lambda x,y:x+y,
             "-":lambda x,y:x-y,
             "*":lambda x,y:x*y,
             "/":lambda x,y:x/y,
             "%":lambda x,y:x%y,
             "^":lambda x,y:x**y
                }

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
            function = OPERATORS[self._value]
            left_value = self._children[0].evaluate_exp()
            right_value = self._children[1].evaluate_exp()
            return function(left_value,right_value)

#exp1=Arithmatic('*',[])
exp2=Arithmatic('1.2',[])
exp3=Arithmatic('5.2',[])
exp4=Arithmatic('*',[exp2,exp3])
exp5=Arithmatic('4.2',[])
exp6=Arithmatic('7.5',[])
exp7=Arithmatic('+',[exp5,exp6])
exp8=Arithmatic('/',[exp4,exp7])
exp9=Arithmatic('2',[])
exp10=Arithmatic('^',[exp9,exp8])

print("The expression is:",exp10.strexp())
print("The evluated value is:",exp10.evaluate_exp())
print("String representation is:",exp10.strep())
print("Depth of this computation graph tree is:",exp10.height())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        