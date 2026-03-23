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
        
        self.clear()

        if sourceCollection is not None:
            for item in sourceCollection:
                self.add(item)


    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        if self.size == 0:
            return True

        return False
    
    def __len__(self):
        """Returns the number of items in self."""
        
        return self.size
    
    def clear(self):
        """Makes self become empty."""

        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0

    def __str__(self):
        """Returns the string representation of self."""
        
        bagString = ""
        
        if self.isEmpty():
            bagString = "{}"
        else:
            for i in range(self.size):
                bagString = bagString + str(self.items[i]) + ", "

            bagString = bagString[: -2] # Chops off extra comma

            bagString = "{" + bagString + "}"

        return bagString

    def count(self, item):
        """Returns the number of isntances of the item in self."""
        
        itemCount = 0

        for i in range(self.size):

            if self.items[i] == item:
                itemCount += 1
                
        return itemCount

    def add(self, item):
        """Adds item to self."""

       # Check if Array is full
        if self.size == len(self.items):
            newArray = Array(len(self.items) * 2)

            # Copy over items
            for i in range(self.size):
                newArray[i] = self.items[i]

            self.items = newArray

        self.items[self.size] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        
        if self.count(item) == 0:
            raise KeyError(f"ERROR: {item} is not in the bag!")

        for i in range(self.size):
            if self.items[i] == item:
                break
        self.items[i] = self.items[self.size - 1]

        self.size -= 1

        if self.size <= (len(self.items) // 4):
            if ArrayBag.DEFAULT_CAPACITY <= (len(self.items) // 2):

                newArray = Array(len(self.items) // 2)

                for i in range(self.size):
                    newArray[i] = self.items[i]

                self.items = newArray

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        if self is other:
            return True

        if type(self) != type(other):
            return False

        if len(self) != len(other):
            return False

        for item in self:
            if self.count(item) != other.count(item):
                return False

        return True

    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        
        newBag = ArrayBag(self)

        for item in other:
            newBag.add(item)

        return newBag
 
        
    def __iter__(self):
        """Supports iteration over a view of self."""
        
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1