class Node(object):
    """
    The basic node class storing a value and a 'next' pointer to the next node
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    """
    The linked list class
    """
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
    
    def delete_tail(self):
        """
        Deletes a node from the end of the list
        """
        temp = self.head
        if self.head != None:
            if self.head.next is None:  # if Head is the only Node in the Linked List
                self.head = None
            else:
                while temp.next.next is not None:  # find the 2nd last element
                    temp = temp.next
                temp.next, temp = (
                    None,
                    temp.next,
                )  # (2nd last element).next = None and temp = last element
        return temp
    
    def isEmpty(self):
        """
        Returns a Boolean after checking whether the list is empty
        """
        return self.head is None  # Return if Head is none
    
    def length(self):
        """
        Returns the length of the list
        """
        ln = 0
        if not self.isEmpty():
            ln+=1
        current = self.head
        if self.head:
            while current.next:
                current = current.next
                ln+=1
        return ln