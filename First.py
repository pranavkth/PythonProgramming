# Binary Trees in Python: Recursive Implementation in Python-- Developer -> Pranav Gupta.

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

# Func to add a key in a tree.

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

# Func to Search For a Key in Tree

    def find(self,key):
        if self.root != None:
            self._find(key,self.root)
        else:
            print"Tree doesent exist"

    def _find(self, key , node):
        if key != node.key and node.left == None and node.right == None:
            print "Key not found"
        else:
            if key == node.key:
                print "key found"
            elif key < node.key:
                self._find(key,node.left)
            elif key > node.key:
                self._find(key,node.right)

# Func to Delete a tree.

    def deleteTree(self):
        self.root = None

# Function to Return the level of a node:

    def level(self,key):
        if self.root != None:
            self._level(key,self.root)

    def _level(self,key,node,level = 1 ):
        result = level

        if key != node.key and node.left == None and node.right == None:
            print "Key not Found"
        else:
            if key == node.key:
                print "level is " + str(result)
            elif key < node.key :
                self._level(key,node.left,result+1)
            elif key > node.key :
                self._level(key,node.right,result+1)

# Func for Height of tree:
    def height(self, node):
        if node == None:
            return 0
        else:
            ldepth = self.height(node.left)
            rdepth = self.height(node.right)
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1

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