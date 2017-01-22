class Node:

# Defines the prperties of a node of the tree.

    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None



class Tree:

# Defines the properties of the Tree.

    def __init__(self):
        self.root = None


# Function to Add A key to the tree.

    def add(self,key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._add(key,self.root)

    def _add(self,key,node):
        if key < node.key:
            if node.left != None:
                self._add(key,node.left)
            else:
                node.left = Node(key)
        else:
            if node.right != None:
                self._add(key,node.right)
            else:
                node.right = Node(key)

# Func to Print a tree.

    def printTree(self):
        if self.root != None:
            self._print(self.root)

    def _print(self,node):
        if node != None:
            print node.key
            self._print(node.left)
            self._print(node.right)

# Func for Traversals:

    def inorder(self):
        if self.root != None:
            self._inorder(self.root)
    def _inorder(self,node):
        if node != None:
            print node.key
            self._inorder(node.left)
            self._inorder(node.right)

# Func to search a given key in the tree:

    def search(self,key):
        if self.root != None:
            self._search(key,self.root)

    def _search(self,key,node):
        if node != None:
            if key != node.key and node.left == None and node.right == None:
                print "key not found"
            else:
                if key == node.key:
                    print "key found"
                elif key < node.key:
                    self._search(key,node.left)
                else:
                    self._search(key,node.right)



t = Tree()
t.add(10)
t.add(02)
t.add(30)









