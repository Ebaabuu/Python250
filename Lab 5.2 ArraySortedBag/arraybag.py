"""
File: arraybag.py
"""

from arrays import Array
from baginterface import BagInterface

class ArrayBag(BagInterface):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 4 #small to force resizing

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""

        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        
        # Copy over items from the provided source
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.size == 0
    
    def __len__(self):
        """Returns the number of items in self."""
       
        return self.size
    
    def clear(self):
        """Makes self become empty."""
        
        # Full reset so we don't waste excess elements
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0    

    def __str__(self):
        """Returns the string representation of self."""
        # Below is the clever Pythonic way
        #return "{" + ", ".join(map(str, self)) + "}"
        
        bagString = ""
        
        if self.size > 0:
                       
            for i in range(0, self.size):
                bagString = bagString + str(self.items[i]) + ", "
        
            # strip off the extra ", " at the end of the last data added
            # Index -1 is the last char in the string, -2 the next to last.
            bagString = bagString[:-2]
            
        bagString = "{" + bagString + "}"
        
        return bagString

    def count(self, item):
        """Returns the number of isntances of the item in self."""
        
        itemCount = 0
        
        for i in self.items:
            if i == item:
                itemCount += 1
                
        return itemCount

    def add(self, item):
        """Adds item to self."""
       
        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            temp = Array(2 * len(self))
           
            for i in range(len(self)):
                temp[i] = self.items[i]
            
            self.items = temp
        
        # Store the new item
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        
        # Check precondition and raise if necessary
        if self.count(item) == 0:
            raise KeyError(str(item) + " not in bag")
        
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
            
        # Move last element over this one
        self.items[targetIndex] = self.items[self.size - 1]
            
        # Decrement logical size
        self.size -= 1
        
        # Check array memory here and decrease it if necessary
        if self.size <= (len(self.items) // 4):
        
            # Don't allow size to go below DEFAULT_CAPACITY
            if ArrayBag.DEFAULT_CAPACITY > len(self.items) // 2:
                newSize = ArrayBag.DEFAULT_CAPACITY
            else:
                newSize = len(self.items) // 2
                
            temp = Array(newSize)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        
        result = ArrayBag(self) #let the constructor do the copy
        
        # copy the items from the other bag
        for item in other:
            result.add(item)
            
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        # Are they the same object?
        if self is other: 
            return True
        
        # Are they the different types?
        if type(self) != type(other): 
            return False
        
        # Do they contain a different number of items?
        if len(self) != len(other):
            return False 
     
        # Do they contain the same items?
        for item in self:
            if not item in other:
                return False
            
        return True    
        
    def __iter__(self):
        """Supports iteration over a view of self."""
        
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1