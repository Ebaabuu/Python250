"""
File: arraystack.py
Author: Ken Lambert
"""

from arrays import Array
from stackinterface import StackInterface

class ArrayStack(StackInterface):
    """An array-based stack implementation."""

    # Class variable
    DEFAULT_CAPACITY = 4 # small to force resizing
   
    def push(self, item):
        """Inserts item at top of the stack."""
        
        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            temp = Array(2 * len(self))
           
            for i in range(len(self)):
                temp[i] = self.items[i]
            
            self.items = temp        
        
        self.items[self.size] = item
        self.size += 1    
   
    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        
        if self.isEmpty():
            raise KeyError("The stack is empty")
        
        return self.items[len(self) - 1]

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self.items[len(self) - 1]
        self.size -= 1
        
        # Check array memory here and decrease it if necessary
        if self.size <= (len(self.items) // 4):
        
            # Don't allow size to go below DEFAULT_CAPACITY
            if ArrayStack.DEFAULT_CAPACITY > len(self.items) // 2:
                newSize = ArrayStack.DEFAULT_CAPACITY
            else:
                newSize = len(self.items) // 2
                
            temp = Array(newSize)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp        
        
        return oldItem
    
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        # Are they the same object?
        if self is other:
            return True

        if self.size != other.size:
            return False
        
        # Bags are the same size, only need 1 index
        for i in range(self.size):
            if self.items[i] != other.items[i]:
                return False
            
        return True
    
    def __add__(self, other):
        
        newStack = ArrayStack(self)
        
        for i in other:
            newStack.push(i)
            
        return newStack
        
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        self.size = 0
        
        # Copy over items from the provided source
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)            
        
    def __len__(self):
        """Returns the number of items in self."""
        return self.size         

    def clear(self):
        """Makes self become empty."""
        
        self.size = 0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)    
    
    def isEmpty(self):
        """Returns True if size is zero,
        or False otherwise."""
        
        return self.size == 0          
            
    def __str__(self):
        """Returns the string representation of self."""
        
        stackString = ""
        
        if self.size > 0:
                       
            for i in range(0, self.size):
                stackString = stackString + str(self.items[i]) + ", "
        
            # strip off the extra ", " at the end of the last data added
            # Index -1 is the last char in the string, -2 the next to last.
            stackString = stackString[:-2]
            
        stackString = "bottom -> {" + stackString + "} <- top"
        
        return stackString
    
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1       