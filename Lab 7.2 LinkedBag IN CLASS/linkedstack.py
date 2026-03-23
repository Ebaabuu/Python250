"""
File: linkedstack.py
"""

from node import Node
from stackinterface import StackInterface
from arrays import Array

class LinkedStack(StackInterface):
    """A link-based stack implementation."""

    def push(self, item):
        """Adds item to the top of the stack."""

        newNodeRef = Node(item)
        newNodeRef.next = self.items
        self.items = newNodeRef
        self.size += 1
    
    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty."""

        if self.isEmpty():
            raise KeyError("ERROR: Can't peek an empty stack.")

        return self.items.data

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack."""

        if self.isEmpty():
            raise KeyError("ERROR: Can't pop an empty stack.")

        backup = self.items.data

        self.items = self.items.next
        self.size -= 1
        return backup
    
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""

        tempArray = Array(self.size)
        index = 0

        curRef = self.items
        while curRef is not None:
            tempArray[index] = curRef.data
            curRef = curRef.next
            index += 1

        for i in range(self.size - 1, -1, -1):
            yield tempArray[i]

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        if self is other:
            return True

        if type(self) != type(other):
            return False

        if self.size != other.size:
            return False

        curNode = self.items
        otherNode = other.items
        while curNode is not None:
            if curNode.data != otherNode.data:
                return False

            curNode = curNode.next
            otherNode = otherNode.next

        return True

    ############################
    # ITEMS BELOW ARE COMPLETE #
    ############################   
    
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.items = None
        self.size = 0
        
        # Copy over items from the provided source
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)      
    
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None    
        
    def __len__(self):
        """Returns the number of items in self."""
        return self.size         

    def isEmpty(self):
        """Returns True if size is zero,
        or False otherwise."""
        
        return self.size == 0                
    
    def __add__(self, other):
        
        newStack = LinkedStack(self)
        
        for i in other:
            newStack.push(i)
            
        return newStack    
        
    def __str__(self):
        """Returns the string representation of self."""
        
        stackString = ""
        
        if self.size > 0:
            
            for i in self:
                stackString = stackString + str(i) + ", "
        
            # strip off the extra ", " at the end of the last data added
            # Index -1 is the last char in the string, -2 the next to last.
            stackString = stackString[:-2]
            
        stackString = "bottom -> {" + stackString + "} <- top"
        
        return stackString  