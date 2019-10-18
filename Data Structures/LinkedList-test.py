from LinkedList import LinkedList, Node
    
def main():
    print()
    print("An empty list initialized...")
    ll = LinkedList()
    print("Is the list empty? ",ll.isEmpty())
    print("Now a list with an initial value...")
    ll = LinkedList(Node(10))
    ll.show()
    print("Is the list empty? ",ll.isEmpty())
    print("Appending at the end...")
    ll.append(Node(20))
    ll.show()
    print("Inserting at the beginning...")
    ll.insert_first(Node(100))
    ll.show()
    print("Deleting the tail...")
    ll.delete_tail()
    ll.show()
    print("Inserting few more nodes...")
    ll.append(Node(25))
    ll.append(Node(50))
    ll.show()
    print("Length of the list:", ll.length())
    print()
    
if __name__ == "__main__":
    main()