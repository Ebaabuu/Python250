"""
File: arrayqueue.py
"""

from arrays import Array
from queueinterface import QueueInterface

class ArrayQueue(QueueInterface):
    """An array-based queue implementation. Treats the array as circular."""

    # Class variable
    DEFAULT_CAPACITY = 4
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""

        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)

        self.front = -1
        self.rear = -1
        self.size = 0
        
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def clear(self):
        """Makes self become empty."""
        
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)

        self.front = -1
        self.rear = -1
        self.size = 0

    def add(self, item):
        """Inserts item at rear of the queue."""
        
        # Double size if filled.
        if self.size == len(self.items):
            
            temp = Array(self.size * 2)
                
            for i in range(self.size):
                temp[i] = self.items[(self.front + i) % len(self.items)]
                
            self.items = temp
            self.front = 0
            self.rear = self.size - 1
        
        # Handle empty queue
        if self.size == 0:
            self.items[0] = item
            self.front = 0
            self.rear = 0
        
        else:
                        
            # Update rear with wrap            
            self.rear = (self.rear + 1) % len(self.items)            
               
            # Store new value
            self.items[self.rear] = item
                        
        
        self.size += 1
    
    def __str__(self):
        """Returns the string representation of self."""
        
        queueString = ""
                
        if self.size > 0:
                       
            for i in range(self.size):
                queueString += str(self.items[(i + self.front) % len(self.items)]) + ", "
        
            # strip off the extra ", " at the end of the last data added
            # Index -1 is the last char in the string, -2 the next to last.
            queueString = queueString[:-2]
            
        queueString = "front -> {" + queueString + "} <- rear"
        
        return queueString

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        
        if self.isEmpty():
            raise KeyError("ERROR: Queue is empty")
        
        return self.items[self.front]

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        
        if self.isEmpty():
            raise KeyError("ERROR: Queue is empty")
        
        poppedItem = self.items[self.front]
        
        if self.size == 1:
            self.front = -1
            self.rear = -1
        
        else:
            self.front = (self.front + 1) % len(self.items) #be sure to wrap!
        
        self.size -= 1
        
        # Cut array size in half if we're using less than 1/4 of the array.
        # In the process, shift front to index 0.
        if self.size <= (len(self.items) // 4) \
           and (len(self.items) // 2) >= ArrayQueue.DEFAULT_CAPACITY:
                
            newSize = len(self.items) // 2
                
            temp = Array(newSize)
            for i in range(self.size):
                temp[i] = self.items[(self.front + i) % len(self.items)]
            self.items = temp
            self.front = 0
            self.rear = self.size - 1
            
        return poppedItem

    def __iter__(self):
        """Supports iteration over a view of self."""
        
        for i in range(self.size):
            yield self.items[(i + self.front) % len(self.items)]

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
               
        if self is other:
            return True
        
        if type(self) != type(other):
            return False
        
        if self.size != other.size:
            return False
        
        #Queues are the same size, only need 1 index
        for i in range(self.size):
            if self.items[(i + self.front) % len(self.items)] != \
               other.items[(i + other.front) % len(other.items)]:
                return False
            
        return True 

    def __add__(self, other):
        """Returns a new instance of the type of self
        containing the contents of self and other."""
        
        newQueue = ArrayQueue(self)
        
        for i in other:
            newQueue.add(i)
            
        return newQueue

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.size == 0
    
    def __len__(self):
        """-Returns the number of items in self."""
        
        return self.size
       



