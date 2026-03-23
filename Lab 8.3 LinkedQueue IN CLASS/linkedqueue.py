"""
File: linkedqueue.py
"""

from node import Node
from queueinterface import QueueInterface

class LinkedQueue(QueueInterface):
    """A link-based queue implementation."""

    def add(self, item):
        """Adds item to the rear of the queue."""
       
        # FINISH ME

        newNode = Node(item)

        if self.isEmpty():
            self.front = newNode

        else:
            self.rear.next = newNode

        self.rear = newNode

        self.size += 1

    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        
        # FINISH ME
        if self.isEmpty():
            raise KeyError("ERROR: Cannot peek an empty queue!")

        return self.front.data

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
       
        # FINISH ME
        if self.isEmpty():
            raise KeyError("ERROR: Cannot pop an empty queue!")

        returnVal = self.front.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1

        return returnVal

    ####################################
    ### FUNCTIONS BELOW ARE COMPLETE ###
    ####################################

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        self.front = None
        self.rear = None
        self.size = 0
                
        if sourceCollection is not None:
            for item in sourceCollection:
                self.add(item)   
                        
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        
        self.front = None
        self.rear = None
        self.size = 0   
        
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.front is None
    
    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.size
        
    def __str__(self):
        """Returns the string representation of self."""
        
        qString = ""
                          
        cur = self.front
        while cur is not None:
            qString = qString + str(cur.data) + ", "
            cur = cur.next
    
        # strip off the extra ", " at the end of the last data added
        # Index -1 is the last char in the string, -2 the next to last.
        qString = qString[:-2]
            
        qString = "front -> {" + qString + "} <- rear"
        
        return qString  

    def __iter__(self):
        """Supports iteration over a view of self."""
        
        cur = self.front
        while cur is not None:
            yield cur.data
            cur = cur.next        

    def __add__(self, other):
        """Returns a new instance of the type of self
        containing the contents of self and other."""
        
        newQ = LinkedQueue(self)
        
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
        
        selfcur = self.front
        othercur = other.front
        
        while selfcur is not None:
            if selfcur.data != othercur.data:
                return False
            selfcur = selfcur.next
            othercur = othercur.next
        
        return True