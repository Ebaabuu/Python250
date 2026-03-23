"""
File: arraylist.py
"""

from arrays import Array
from listinterface import ListInterface

class ArrayList(ListInterface):
    """A link-based list implementation."""

    # Class variable
    DEFAULT_CAPACITY = 4 # small to force resizing

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.items = Array(ArrayList.DEFAULT_CAPACITY)
        self.size = 0
        
        # Copy over items from the provided source
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)            
        
    def __len__(self):
        """Returns the number of items in self."""
        return self.size         

    def clear(self):
        """Makes self become empty."""
        
        self.size = 0
        self.items = Array(ArrayList.DEFAULT_CAPACITY)    
    
    def isEmpty(self):
        """Returns True if size is zero,
        or False otherwise."""
        
        return self.size == 0          
            
    def __str__(self):
        """Returns the string representation of self."""
        
        listString = ""
        
        if self.size > 0:
                       
            for i in range(0, self.size):
                listString = listString + str(i) + ". " + str(self.items[i]) + "\n"
      
        return listString
    
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1 


    def add(self, item):
        """Inserts item at the end of the list."""
        
        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            temp = Array(2 * len(self))
           
            for i in range(len(self)):
                temp[i] = self.items[i]
            
            self.items = temp        
        
        self.items[self.size] = item
        self.size += 1    

    def insert(self, index, item):
        """Inserts the item at position i."""
        
        if index < 0: 
            index = 0
        
        elif index > len(self): 
            index = len(self)
            
        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            temp = Array(2 * len(self))
           
            for i in range(len(self)):
                temp[i] = self.items[i]
            
            self.items = temp
            
        # Shift to open insert location
        i = self.size - 1
        while i >= index:
            self.items[i + 1] = self.items[i]
            i -= 1
        
        self.items[index] = item
        self.size += 1
        

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        
        if i == None: 
            i = len(self) - 1
        
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        
        oldItem = self.items[i]
       
        # Shift to fill the hole
        for j in range(i, self.size):
            self.items[j] = self.items[j + 1]
        
        self.size -= 1
        
        # Check array memory here and decrease it if necessary
        if self.size <= (len(self.items) // 4):
        
            # Don't allow size to go below DEFAULT_CAPACITY
            if ArrayList.DEFAULT_CAPACITY > len(self.items) // 2:
                newSize = ArrayList.DEFAULT_CAPACITY
            else:
                newSize = len(self.items) // 2
                
            temp = Array(newSize)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp        
        
        return oldItem

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        
        return self.items[i]

    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        
        self.items[i] = item 
    
    def replace(self, index, item):
        """Preconditions: 0 <= i < len(self)
        Replaces the items at the given position with item.
        Raises: IndexError.
        """
        
        self[index] = item
    
    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
            
        for i in range(self.size):
            if self.items[i] == item:
                return i
            
        raise ValueError(f"{item} was not found in the list.")
    
    def remove(self, item):
        """Precondition: item is in self.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        
        index = self.index(item)
        
        self.pop(index)
            