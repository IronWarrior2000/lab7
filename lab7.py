#Bill Nguyen | Lab 7 | 11/5/24

class Node:
    def __init__(self, value = None, next = None, previous = None):
        # Define the node's basic properties "value", "next", "previous" and default them
        # You will want these to be private properties and the given functions will manipulate them
        # Private properties are defined with 2 underscores like value
        self.__value__ = value
        self.__next__ = next
        self.__previous__ = previous
        # Return this node
        return

    
    def set(self, value):
        # Set this node's value to the given value
        self.__value__ = value

    
    def get_value(self):
        # Return the value of this node
        return self.__value__
    
    def get_next(self):
        # Return this node's next node
        return self.__next__
    
    def get_previous(self):
        # Return this node's previous node
        return self.__previous__
    
    def set_next(self, next):
        # Set this node's next node
        self.__next__ = next
        # Return this node
        return
    
    def set_previous(self, previous):
        # Set this node's previous node
        self.__previous__ = previous
        # Return this node
        return

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.set_next(node2)
node2.set_next(node3)

def getNode(head):
    current = head
    while current:
        print(current.__value__, "->")
        current = current.get_next()
    print(None)

getNode(node1)