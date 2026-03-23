"""
File: linkedbst.py
"""

from bstinterface import BSTInterface
from bstnode import BSTNode
from linkedqueue import LinkedQueue

class LinkedBST(BSTInterface):
    """An link-based binary search tree implementation."""

    def iterativeAdd(self, item):

        newNode = BSTNode(item)
        # STEP 1
        if self.isEmpty():
            self.root = newNode
        else:
            child = self.root
            parent = child
            while child is not None:
                parent = child
                if item < parent.data:
                    child = parent.left
                else:
                    child = parent.right

            if item < parent.data:
                parent.left = newNode
            else:
                parent.right = newNode

        self.size += 1
   
    def __countHeight(self, node):
        
        # STEP 2
        
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        if self.__countHeight(node.left) > self.__countHeight(node.right):
            return self.__countHeight(node.left) + 1
        else:
            return self.__countHeight(node.right) + 1
    
    def __isBalanced(self, node):
        
        if node is None:
            return True
        else:
            if abs(self.__countHeight(node.left) - self.__countHeight(node.right)) > 1:
                return False
            else:
                if self.__isBalanced(node.left) and self.__isBalanced(node.right):
                    return True
                else:
                    return False
      
    ####################################
    ### FUNCTIONS BELOW ARE COMPLETE ###
    ####################################

    def balanced(self):
        
        return self.__isBalanced(self.root)

    def height(self):
        
        return self.__countHeight(self.root)

    def __inorderHelper(self, node, lyst):
        # Recursive helper function for inorder(). Peforms the traversal.
        
        if node != None:
            self.__inorderHelper(node.left, lyst)
            lyst.append(node.data)
            self.__inorderHelper(node.right, lyst)
            
    def levelorder(self):
        """Supports a levelorder (aka breadth first) traversal on a view of self.
        Returns a list containing the node data in level order."""
        
        result = []
        
        if self.root != None:
            
            q = LinkedQueue()
            q.add(self.root)
                
            while not q.isEmpty():
                curRef = q.pop()
                result.append(curRef.data)
    
                if curRef.left:
                    q.add(curRef.left)
                if curRef.right:
                    q.add(curRef.right)

        return result    
    
    def __findHelper(self, node, item):
        
        if node is None:
            return None
        elif node.data == item:
            return node.data
        elif node.data > item:
            return self.__findHelper(node.left, item)
        else:
            return self.__findHelper(node.right, item)  
        
    def __removeNode(self, node):
        
        # Scenario 1: node to remove is a leaf.
        if node.left is None and node.right is None:
            return None

        # Scenario 2: node to remove has only 1 child
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        # Scenario 3: node to remove has 2 children. Replace the item in the
        # node with its in order successor (ios).
        else:
            ios = node.right
            while ios.left is not None:
                ios = ios.left

            ios_data = ios.data

            self.remove(ios_data)

            node.data = ios_data
            
            return node    

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.clear()
        
        if sourceCollection != None:
            for i in sourceCollection:
                self.iterativeAdd(i)
    
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.root == None
    
    def __strHelper(self, node, level):
        
        s = ""
        if node != None:
            s += self.__strHelper(node.right, level + 1)
            s += "| " * level
            s += str(node.data) + "\n"
            s += self.__strHelper(node.left, level + 1)
        return s        
    
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        
        return self.__strHelper(self.root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        
        return iter(self.preorder())

    def __preorderHelper(self, node, lyst):
        
        if node != None:
            lyst.append(node.data)
            self.__preorderHelper(node.left, lyst)
            self.__preorderHelper(node.right, lyst)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        lyst = list()
        self.__preorderHelper(self.root, lyst)
        return lyst

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        self.__inorderHelper(self.root, lyst)
        return lyst

    def __postorderHelper(self, node, lyst):
        
        if node != None:
            self.__postorderHelper(node.left, lyst)
            self.__postorderHelper(node.right, lyst)
            lyst.append(node.data)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
        self.__postorderHelper(self.root, lyst)
        return lyst

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
            
        return self.__findHelper(self.root, item)

    def clear(self):
        """Makes self become empty."""
        
        self.root = None
        self.size = 0
    
    def add(self, item):
        """Adds item to the tree."""
    
        self.iterativeAdd(item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        
        if not item in self:
            raise KeyError("Item not in tree.""")
        
        self.root = self.__locateItemAndRemove(self.root, item)

    def __locateItemAndRemove(self, subTree, itemToRemove):
        
        # If we don't find the target in the tree
        if subTree == None:
            return None
            
        # Found the target in the root of this subtree
        if subTree.data == itemToRemove:
            self.size -= 1
            return self.__removeNode(subTree)

        else:
            if subTree.data > itemToRemove:
                subTree.left = self.__locateItemAndRemove(subTree.left, itemToRemove)
            else:
                subTree.right = self.__locateItemAndRemove(subTree.right, itemToRemove)
                
            return subTree

    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.size

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        if self is other:
            return True
        
        if type(self) != type(other):
            return False
        
        if len(self) != len(other):
            return False
        
        # We only care about containing the same values, not the actual struture.
        if self.inorder() != other.inorder():
            return False
        
        return True
    
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.root == None   