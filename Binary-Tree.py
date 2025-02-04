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

    def __init__(self):
        self.root = None

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

def main():
    bst = BinarySearchTree()
 
    while True:
        print("1. Insert")
        print("2. Search")
        print("3. Print")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the value to insert: "))
            bst.insert(value)
        elif choice == 2:
            value = int(input("Enter the value to search: "))
            print("Value found" if bst.search(value) else "Value not found")
        elif choice == 3:
            print("Tree:")
            bst.printTree()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
    print("Exiting...")
    
main()