#Binary Search Tree
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insertNode(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insertNode(value)
        elif value >= self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insertNode(value)

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)
        else:
            return True

    def printTree(self): #Inorder Traversal
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()

class BinarySearchTree:

    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insertNode(value)

    def search(self, value):
        if self.root is None:
            return False
        return self.root.search(value)

    def printTree(self):
        if self.root is None:
            return
        self.root.printTree()

#Test
bst = BinarySearchTree(5)
bst.insert(4)
bst.insert(6)
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(7)
bst.insert(5)

bst.printTree()

print(bst.search(3)) #True
print(bst.search(8)) #False