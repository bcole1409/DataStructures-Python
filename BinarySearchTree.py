class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None #null
        self.right = None #null

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        #New Node
        NewNode = Node(data)
        if self.root == None:
            self.root = NewNode
            
        else:
            currentNode = self.root
            while currentNode != None:
                print(currentNode.data)
                if currentNode.data > data:
                    currentNode = currentNode.left
                elif currentNode.data == data:
                    break #do nothing already in tree
                else:
                    currentNode = currentNode.right
                   
            currentNode = NewNode

    def printTree(self):
        if self.root != None:
            self.helperPrint(self.root)

    #HELPER FUNCTION RELATED TO PRINT FUNCTION
    def helperPrint(self, Cur_Node):
        if Cur_Node != None:
            self.helperPrint(Cur_Node.left)
            print(Cur_Node.data)
            self.helperPrint(Cur_Node.right) 


def main():
    Tree = BST()
    #test
    for i in range(0,5):
        Tree.insert(int(input()))

    Tree.printTree()

if __name__ == "__main__":
    main()   
