class BST: #BinarySearchTree
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def insert(self,data):   #self.key is the root
        if self.key is None:  #if root is None then you can store the value of root as data
            self.key = data
            return
        if self.key == data:  #checks if root and data is same
            return
        """if data is less than root , if data is smaller you place it in left 
        but there's two scenarios, 1. left sub tree is empty 2. left sub tree is not empty"""
        if self.key > data:   #if root is greater than data
            if self.left:   #checks whether there's a values in the left node, return true if it exist and false if it doesn't
                self.left.insert(data) #if it's true, then recursion should be done
            else:
                self.left = BST(data) #if there's no node in the left, we're inserting new node by calling BST to create a new node
        elif self.key < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data) #if there's no node in the right, we're inserting new node by calling BST to create a new node as data
    def search(self,data):
        if self.key==data:
            print("node is found")
            return
        if data < self.key: #two scenarios, 1.  left child is there  2. left child is not there
            if self.left:
                self.left.search(data)
            else:
                print("no node found")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("no node is found")

root = BST(None) #initialising root values as None
root.insert(20)  #calling insert method, object is root and data of new node is 20
list1=[23,56,23,65,21,62]
for i in list1:
    root.insert(i)
root.search(56)
root.search(20)
root.search(101)



