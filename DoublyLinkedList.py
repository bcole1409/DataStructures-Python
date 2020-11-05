class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None #null
        self.prev = None #null

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self,data):
        NewNode = Node(data)
        if self.head = None:
            self.head = NewNode
        else:
            current = self.head
            while(current.next != None):
                current.prev = current.next
                current = current.next
            current.next = NewNode
