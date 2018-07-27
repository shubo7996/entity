class Node:
    def __init__(Self, node_value ):
        self.data = node_value
        self.head = None
        self.trail = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.trail = None

    #def Push(head, trail, node_value, prevNode):
    #    new_node = Node(node_value)
    #    new_node.head = 

    def insertNode(self node_value):
        #counter+=1
        new_node = Node(node_value)
        if not self.head:
            self.head = new_node.head
        else:
            self.trail.next = new_node

        self.trail = new_node
            
    def insertNodeAtAnyPosition(self,head,node_value,counter):






    def append(self,node_value):
        new_node = Node(node_value)
        last = self.head
        while(1):
            if last == new_node.head:
                last.head = new_node
                break
        last = last.next
