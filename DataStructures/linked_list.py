class Node:
    """
    An object for storing a single node of a linked list.
    Models to attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data 

    def __repr__(self):

        return "<Node data: %s" % self.data
    
"""N1 = Node(10)
print(N1)
N2 = Node(20)
N1.next_node = N2
print(N1.next_node)"""

class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None    
    
    def size(self):
        """
        Returns the number of nodes in the linked list and it runs in Linear Time
        """
        current = self.head
        count = 0
         
        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        """
        Adds a new node containing data at the head of the list, it takes O(1) time (Constant Time) 
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        search for the first node containing dat THT MATCHES  the key.
        Return the node or 'None' if not found.
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data as index position
        Inserion takes O(1) trime but finding the node at the insertion point takes linear time.
        Hence overall it takes linear time O(n)
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position = position - 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes the Node containing data that atches the key.
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current
    
    def node_at_index(self, index):
        """
        returns the node value at given index
        """
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position +=1
            return current

    def __repr__(self):
        """
        Return a string representation of the lsit
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '-> '.join(nodes)

""" Test Adding node
l = LinkedList()
N1 = Node(10)
l.head = N1
l.add(1)
print(l.size())"""

"""Test Repr Function that returns the entire linked list when called
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l)"""

"""
Test Searching
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(15)

print(l.search(11))
"""

"""
#Test Inserting a node at a given position
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(15)
l.insert(5, 2)
print(l)"""

"""
#Test Remove function
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(15)
l.remove(2)
print(l)"""

