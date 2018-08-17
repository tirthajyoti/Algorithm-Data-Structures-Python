# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:26:42 2018
@author: Tirtha
"""

from Common_data_structures_class import Stack, Queue, Tree, Arithmatic

###Test code for Stack
###======================================================
init_list=[11,22,33,44]
print("Initializing stack with a list:",init_list)
s1 = Stack(init_list)
s1.draw()
print("height of the stack:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("height of the stack now:",s1._height)
print("Pushing 20...")
s1.push(20)
print("Pushing 30...")
s1.push(30)
s1.draw()
print("height of the stack now:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("Height now:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("Height now:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("Height now:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("Height now:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("Height now:",s1._height)
print("Popping the top of the stack:",s1.pop())
print("Height now:",s1._height)
print("Is the stack empty?",s1.isEmpty())
print("Pushing a float")
s1.push(3.56)
print("Pushing a string")
s1.push("Hello")
s1.draw()
print("Popping the top of the stack:",s1.pop())
print("Popping the top of the stack:",s1.pop())
print("Is the stack empty?",s1.isEmpty())

###Test code for Queue
###======================================================
init_list=[99,98,97,96]
print("Initializing queue with a list:",init_list)
q1 = Queue(init_list)
q1.draw()
print("Length of the queue:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length of the queue now:",q1._length)
print("Enqueing 20...")
q1.enqueue(20)
print("Enqueing 30...")
q1.enqueue(30)
q1.draw()
print("Length of the queue now:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length now:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length now:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length now:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length now:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length now:",q1._length)
print("Dequeing from the queue:",q1.dequeue())
print("Length now:",q1._length)
print("Is the queue empty?",q1.isEmpty())
print("Enqueing a float")
q1.enqueue(3.56)
print("Enqueing a string")
q1.enqueue("Hello")
q1.draw()
print("Dequeing from the queue:",q1.dequeue())
print("Dequeing from the queue:",q1.dequeue())
print("Is the queue empty?",q1.isEmpty())

###Test code for Tree
###======================================================
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

###Test code for Arithmatic
###======================================================
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