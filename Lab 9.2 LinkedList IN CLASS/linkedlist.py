"""
File: linkedlist.py
"""

from node import Node
from listinterface import ListInterface

class LinkedList(ListInterface):
    """A link-based list implementation."""

    def add(self, item):
        """Inserts item at the end of the list."""
        
        # FINISH ME
        newNode = Node(item)

        if self.isEmpty():
            self.head = newNode

        else:
            self.tail.next = newNode

        self.tail = newNode
        self.size += 1

    # Helper method returns node at position i.
    # No docstring comment because this isn't intended
    # to be used by the outside world.
    def getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        
        # FINISH ME
        if i < 0 or i >= self.size:
            return None

        curNode = self.head
        counter = 0
        while curNode is not None:
            if counter == i:
                return curNode
            curNode = curNode.next
            counter += 1

    def insert(self, i, item):
        """Inserts the item at position i."""

        newNode = Node(item)

        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)

        if i == self.size:
            self.add(item)

        elif i == 0:
            newNode.next = self.head
            self.head = newNode
            self.size += 1

        else:
            prevNode = self.getNode(i - 1)
            newNode.next = prevNode.next
            prevNode.next = newNode
            self.size += 1

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        
        if i is None:
            i = self.size - 1

        if i < 0 or i > self.size - 1:
            raise IndexError("ERROR: Invalid index in pop().")

        if i == 0:
            backup = self.head.data
            self.head = self.head.next

            if self.head is None:
                self.tail = None

        else:
            prevNode = self.getNode(i - 1)
            backup = prevNode.next.data

            prevNode.next = prevNode.next.next

            if prevNode.next is None:
                self.tail = prevNode

        self.size -= 1

        return backup

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""

        if i < 0 or i > self.size - 1:
            raise IndexError("ERROR: Invalid index in []")
        return self.getNode(i).data

    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""

        if i < 0 or i > self.size - 1:
            raise IndexError("ERROR: Invalid index in []")

        self.getNode(i).data = item
    
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
            if self[i] == item:
                return i

        raise ValueError(f"{item} is not the item you were looking for.")
    
    def remove(self, item):
        """Precondition: item is in self.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        
        i = self.index(item)

        self.pop(i)
    
    ####################################
    ### FUNCTIONS BELOW ARE COMPLETE ###
    ####################################
    
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""

        self.head = self.tail = None
        self.size = 0
        
        if sourceCollection is not None:
            for i in sourceCollection:
                self.add(i)    
   
    def __iter__(self):
        """Supports iteration over a view of self."""
        
        cursor = self.head
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next
 
    def __str__(self):
        """Returns the string representation of self."""
        
        listString = ""

        count = 0
        for i in self:
            listString += str(count) + ". " + str(i) + "\n"
            count += 1
        
        return listString
   
    def clear(self):
        """Makes self become empty."""
        
        self.head = self.tail = None
        self.size = 0        

    def isEmpty(self):
            """Returns True if len(self) == 0, or False otherwise."""
            
            return self.size == 0
        
    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.size
    