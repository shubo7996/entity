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

    def append(self, node_data):
        new_node = Node(node_data)
        last = self.head
        while(1):
            if last.next == None:
                last.next = new_node
                break
            last = last.next

     def insertNodeAtAnyPosition(self, prevNode, node_value):
        new_node = Node(node_value)
        new_node.next = prevNode.next
        prevNode.next = new_node


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
print("\n")
obj.append(10)
obj.insertNodeAtAnyPosition(obj.head,5)
print("\n")
obj.printList() 