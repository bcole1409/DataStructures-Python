class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None #null

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    ###########################INSERT/DELETE METHODS##################################
    #ADD NODE TO BEGINNING OF LINKEDLIST
    def insertFirst(self,data):
        NewNode = Node(data)

        #if list is empty
        if self.head == None:
            self.size = 1
            self.head = NewNode
        else:
            #NewNode points to linkedlist
            NewNode.next = self.head
            #set new node to head
            self.head = NewNode
            #add 1 to size of linkedlist
            self.size += 1

    #ADD NODE TO END OF LINKEDLIST     
    def insert(self, data):
        #New Node
        NewNode = Node(data)
        #if list is empty
        if self.head == None:
            self.head = NewNode
            self.size = 1
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = NewNode
            self.size += 1

    #DELETE LAST NODE
    def delete(self):
        #if list is empty
        if self.head == None:
            return
        else:
            #TRAVERSE
            current = self.head
            while(current.next.next != None):
                current = current.next
            current.next = None
            #reduce size of list
            self.size -= 1

###############################################################################

#################################PRINT METHODS#################################
    def printList(self):
        if self.head == None:
            print("List is Empty")
        else:
            current = self.head
            print(current.data)
            while(current.next != None):
                current = current.next
                print(current.data)

    def getSize(self):
        print(self.size)

###############################################################################


    

def main():
    List = LinkedList()
    N = int(input())
    for i in range(0,N):
        List.insert(int(input()))

        
    

    #function works
    #List.insertFirst(10)
    #List.printList()
    #List.getSize()
    List.printList()
    List.delete()
    List.printList()
    

if __name__ == "__main__":
    main()
            
        

