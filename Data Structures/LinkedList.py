# Linked List in Python

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#=====================================

class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_node):
        """
        Appends a new node at the end
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def show(self):
        """
        Shows (prints) a linked list
        """
        print('[',end='')
        current = self.head
        if self.head:
            if current.next:
                print(self.head.value,end=', ')
            else:
                print(self.head.value,end='')
        while current.next:
            current = current.next
            if current.next:
                print(current.value,end=', ')
            else:
                print(current.value,end='')
        print(']')
        
    def insert_first(self, new_node):
        """
        Inserts a new node at the beginning
        """
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        """
        Deletes a node from the beginning
        """
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None