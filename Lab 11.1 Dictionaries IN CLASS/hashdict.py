"""
File: hashdict.py
"""

from entry import Entry
from arrays import Array
from dictinterface import DictInterface

class HashDict(DictInterface):
    """Represents a hash-based dictionary."""

    # intentionally small
    DEFAULT_CAPACITY = 5

    # Returns the hash index of the given key for a table of 
    # tableSize. Assumes key is an integer.    
    def __hash(self, key):
        
        return key % self.capacity
       
    def add(self, key, value):
        """Adds the key/value pair to the dictionary."""

        entry = Entry(key, value)

        hashIndex = self.__hash(key)

        # Handle adding new first node in chain
        if (self.hashTable[hashIndex] is None or
                self.hashTable[hashIndex].key >= key):
            entry.next = self.hashTable[hashIndex]
            self.hashTable[hashIndex] = entry

        # Handle adding a node anywhere after the first node in the chain
        else:
            prevRef = self.hashTable[hashIndex]
            curRef = self.hashTable[hashIndex].next

            while curRef is not None and entry.key > curRef.key:
                prevRef = curRef
                curRef = curRef.next

            prevRef.next = entry
            entry.next = curRef

        self.size += 1

    def __iter__(self):
        """Serves up the entries in the dictionary in ascending order of
        key value."""
        
        for index in range(self.capacity):
            curRef = self.hashTable[index]

            while curRef is not None:
                yield curRef
                curRef = curRef.next

    def get(self, key, defaultValue = None):
        
        """Returns the associated value if the key is in the dictionary, or returns the default value otherwise."""
        
        hashIndex = self.__hash(key)
        curRef = self.hashTable[hashIndex]

        while curRef is not None and curRef.key <= key:
            if curRef.key == key:
                return curRef.value
            curRef = curRef.next

        return defaultValue

    def pop(self, key, defaultValue=None):
        """Removes the key and returns the associated value if the key is in the dictionary, or returns the default value otherwise."""
    
        hashIndex = self.__hash(key)
        curRef = self.hashTable[hashIndex]

        if curRef is None:
            return defaultValue

        if curRef.key == key:
            self.hashTable[hashIndex] = curRef.next
            self.size -= 1
            return curRef.value

        prevRef = curRef
        curRef = curRef.next

        while curRef is not None and curRef.key <= key:
            if curRef.key == key:
                prevRef.next = curRef.next
                self.size -= 1
                return curRef.value
            prevRef = curRef
            curRef = curRef.next

        return defaultValue
    
    ################################
    # FUNCTIONS BELOW ARE COMPLETE #
    ################################

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.size == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        
        return self.size
        
    def __str__(self):
        """Returns the string representation of self with one entry per line in ascending order of key value."""
        
        result = "<hash, key, value>\n"
        
        for entry in self:
            result += "<" 
            result += str(self.__hash(entry.key)) + ", "
            result += str(entry.key) + ", " + str(entry.value) 
            result += ">" + "\n"
        return result

    def __init__(self, keys = None, values = None,
                 capacity = None):
        """Will copy entries to the dictionary
        from keys and values if they are present."""
        
        if capacity is None:
            self.capacity = HashDict.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        
        self.hashTable = Array(self.capacity)
        
        self.size = 0
        
        # Add pairs from key and values to the dictionary
        if keys and values:
            valuesIter = iter(values)
            for key in keys:
                self.add(key, next(valuesIter))
        
    def clear(self):
        """Makes self become empty."""
    
        self.hashTable = Array(self.capacity)
        self.size = 0