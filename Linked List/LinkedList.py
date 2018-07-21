class  Node:
    def __init__(self,node_data):
        self.data = node_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self,node_data):
        new_node = Node(node_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        l=self.head
        while(l):
            if l == None:
                break
            print (l.data, end= " ")
            l = l.next

obj = LinkedList()
obj.Push(1)
obj.Push(3)
obj.Push(6)
obj.printList()