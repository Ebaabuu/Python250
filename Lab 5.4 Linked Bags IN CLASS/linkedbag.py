"""
File: linkedbag.py
"""

from baginterface import BagInterface
from node import Node

class LinkedBag(BagInterface):
    """A link-based bag implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.clear()

        if sourceCollection is not None:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return (self.size == 0)
    
    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.size

    def clear(self):
        """Makes self become empty."""
        
        self.size = 0
        self.head = None

    def add(self, item):
        """Adds item to self."""
        
        newNodeRef = Node(item)
        newNodeRef.next = self.head
        self.head = newNodeRef

        self.size += 1

    def __str__(self):
        """Returns the string representation of self."""

        # Below is the clever Pythonic way
        #return "{" + ", ".join(map(str, self)) + "}"
        
        bagString = ""
        
        if self.size > 0:

            currentNode = self.head
            while currentNode is not None:
                bagString += str(currentNode.data) + ", "
                currentNode = currentNode.next

        bagString = bagString[:-2]
                    
        bagString = "{" + bagString + "}"
        
        return bagString 
    
    def count(self, item):
        """Returns the number of instances of the item in the bag."""

        count = 0
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == item:
                count += 1
            currentNode = currentNode.next

        return count

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        
        # item is not in the bag
        if self.count(item) == 0:
            raise KeyError(f"ERROR: Cannot remove {item} from the bag!")

        # locate node with item to remove
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == item:
                break
            currentNode = currentNode.next

        # swap node data to delete with head node data
        currentNode.data, self.head.data = self.head.data, currentNode.data

        # remove current head node
        self.head = self.head.next

        self.size -= 1

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
        
        newBag = LinkedBag(self)

        currentNode = other.head
        while currentNode is not None:
            newBag.add(currentNode.data)
            currentNode = currentNode.next

        return newBag

    def __iter__(self):
        """Supports iteration over a view of self."""
        
        cursor = self.head
        while cursor != None:
            yield cursor.data
            cursor = cursor.next