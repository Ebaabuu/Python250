"""
File: linkedbag.py
"""

from baginterface import BagInterface
from node import Node

class LinkedBag(BagInterface):
    """A link-based bag implementation."""

    def __init__(self, sourceCollection = None, tail = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.head = None
        self.size = 0
        
        # STEP 2
        self.tail = None
       
        # Copy over all items from source
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.size == 0
    
    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.size

    def clear(self):
        """Makes self become empty."""
        
        self.head = None
        self.size = 0
        
        # STEP 3
        self.tail = None


    def add(self, item):
        """Adds item to self."""
        
        # STEP 4
        newNodeRef = Node(item)
        if self.head is None:
            self.head = newNodeRef
            self.tail = newNodeRef
        else:
            self.tail.next = newNodeRef
            newNodeRef.prev = self.tail
            self.tail = newNodeRef

        self.size += 1

        

    def __str__(self):
        """Returns the string representation of self."""

        # Below is the clever Pythonic way
        #return "{" + ", ".join(map(str, self)) + "}"
        
        bagString = ""
        
        if self.size > 0:
            curNode = self.head
            while curNode != None:
                bagString = bagString + str(curNode.data) + ", "
                curNode = curNode.next        
        
            # strip off the extra ", " at the end of the last data added
            # Index -1 is the last char in the string, -2 the next to last.
            bagString = bagString[:-2]
            
        bagString = "{" + bagString + "}"
        
        return bagString 
    
    def count(self, item):
        """Returns the number of instances of the item in the bag."""
        
        itemCount = 0
        
        curNode = self.head
        while curNode != None:
            if curNode.data == item:
                itemCount += 1
            curNode = curNode.next
                
        return itemCount  

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        
        # Check precondition and raise if necessary
        if self.count(item) == 0:
            raise KeyError(str(item) + " not in bag")
        
        # Remove the head node
        if self.head.data == item:
            self.head = self.head.next
            
            # STEP 5
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

            
        # Remove a non-head node
        else:
            curNode = self.head
            prevNode = None
            while curNode is not None:
                if curNode.data == item:
                    break
                else:
                    prevNode = curNode
                    curNode = curNode.next
            
            # STEP 5
            if curNode.next is not None:
                curNode.next.prev = prevNode
                prevNode.next = curNode.next
            else:
                self.tail = prevNode
                self.tail.next = None
            
            prevNode.next = curNode.next
        
        # Decrement logical size
        self.size -= 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = LinkedBag(self)
        
        # Note we get other's items in the new bag first
        # Doesn't matter in this case since the order doesn't
        # matter.
        curNode = other.head
        while curNode != None:
            result.add(curNode.data)
            curNode = curNode.next
            
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
        
        cursor = self.head
        while cursor != None:
            yield cursor.data
            cursor = cursor.next