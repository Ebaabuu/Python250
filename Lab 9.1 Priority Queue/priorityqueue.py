"""
File: priorityqueue.py
"""

from queueinterface import QueueInterface
from arraylist import ArrayList
from priorityitem import PriorityItem

class PriorityQueue(QueueInterface):
    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        # STEP 3
        self.list = ArrayList()
                
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                        
    # Helper function. Given an item, it finds the index of the first item
    # in the ArrayList with a priority value >= the item. That index is the position
    # where item should be added to the list. It returns that index.
    # Raises ValueError if item is not PriorityItem type.
    def findInsert(self, item):
        
        tempItem = PriorityItem(1, "dummy")
        
        if type(item) != type(tempItem):
            raise ValueError(f"findInsert() can only be used with PriorityItem type. Your type was {type(item)}.")
        
        # STEP 4
        if self.list.size == 0:
            return 0

        if item.priority >= self.list[len(self.list) - 1].priority:
            return len(self.list)

        for i in range(len(self.list)):
            if item.priority <= self.list[i].priority:
                return i
    
    def add(self, item):
        """Adds priority item to the rear of the proper location in the queue."""
       
        # STEP 5
        self.list.insert(self.findInsert(item), item)

    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        
        # STEP 6
        return self.list[0]

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
       
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        
        # STEP 7
        return self.list.pop(0)

    def __iter__(self):
        """Supports iteration over a view of self."""
        
        for i in range(self.list.size):
            yield self.list[i]    

    def __str__(self):
        """Returns the string representation of self."""
        
        queueString = ""
                        
        if self.list.size > 0:
                       
            for i in range(self.list.size):
                queueString += str(self.list[i]) + "\n"
                
        return queueString

    def __add__(self, other):
        """Returns a new instance of the type of self
        containing the contents of self and other."""
        
        newQ = PriorityQueue(self)
        
        for i in other:
            newQ.add(i)
        
        return newQ

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        if self is other:
            return True
        
        if type(self) != type(other):
            return False
        
        if len(self) != len(other):
            return False
              
        for i in range(self.list.size):
            if self.list[i] != other.list[i]:
                return False
        
        return True

    def clear(self):
        """Makes self become empty."""
        
        self.list = ArrayList()
        
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.list.size == 0
    
    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.list.size    
