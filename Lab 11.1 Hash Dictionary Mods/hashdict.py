"""
File: hashdict.py
"""

from entry import Entry
from node import Node
from arrays import Array
from dictinterface import DictInterface

class HashDict(DictInterface):
    """Represents a hash-based dictionary."""

    # intentionally small
    DEFAULT_CAPACITY = 5

    def __str__(self):
        """Returns the string representation of self with one entry per line in ascending order of key value."""
        returnVal = ""
        for i in range(self.capacity):
            curNode = self.hashTable[i]
            returnVal += f"{i}: "
            if curNode is None:
                returnVal += "None\n"
            else:
                while curNode is not None:
                    returnVal += f"({curNode.key}, {curNode.value})"
                    if curNode.next is not None:
                        returnVal += " -> "
                    curNode = curNode.next
                returnVal += "\n"
        return returnVal
    
    def contains(self, key, value):
                
        hashIndex = self.__hash(key)
        curNode = self.hashTable[hashIndex]

        while curNode is not None:
            if curNode.value == value and curNode.key == key:
                return True
            curNode = curNode.next
        return False
    
    def __eq__(self, otherDict):
        
        if self is otherDict:
            return True

        if type(self) != type(otherDict):
            return False

        if self.size != otherDict.size:
            return False

        for item in self:
            if not otherDict.contains(item.key, item.value):
                return False

        return True
    

    # Returns the hash index of the given key for a table of 
    # tableSize. Assumes key is an integer.    
    def __hash(self, key):
        
        return key % self.capacity
       
    def add(self, key, value):
        """Adds the key/value pair to the dictionary."""

        entry = Entry(key, value)

        hashIndex = self.__hash(entry.key)
        
        # Handle first node add
        if self.hashTable[hashIndex] is None or self.hashTable[hashIndex].value >= entry.value:
            entry.next = self.hashTable[hashIndex]
            self.hashTable[hashIndex] = entry
        
        # Any later node add
        else:
            prevRef = self.hashTable[hashIndex]
            chainRef = self.hashTable[hashIndex].next
            
            while chainRef != None:
            
                # Stop when chainRef is larger or equal to entry.
                # Then we'll link entry as the next node after prevRef
                if chainRef.key >= entry.key:
                    break
                prevRef = chainRef
                chainRef = chainRef.next
                
            prevRef.next = entry
            entry.next = chainRef
        
        self.size += 1

    def __iter__(self):
        """Serves up the entries in the dictionary in ascending order of
        key value."""
        
        for index in range(self.capacity):
            currentNode = self.hashTable[index]
            
            while currentNode is not None:
                yield currentNode
                currentNode = currentNode.next

    def get(self, key, defaultValue = None):
        
        """Returns the associated value if the key is in the dictionary, or returns the default value otherwise."""
        
        hashIndex = self._HashDict__hash(key)
        currentNode = self.hashTable[hashIndex]
    
        while currentNode is not None and currentNode.key <= key:
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next
    
        return defaultValue

    def pop(self, key, defaultValue=None):
        """Removes the key and returns the associated value if the key is in the dictionary, or returns the default value otherwise."""
    
        hashIndex = self.__hash(key)
        currentNode = self.hashTable[hashIndex]
    
        # Bucket is empty, key is not in dictionary
        if currentNode is None:
            return defaultValue
    
        # If the first node in the chain has a matching key
        if currentNode.key == key:
            self.hashTable[hashIndex] = currentNode.next
            self.size -= 1
            return currentNode.value
    
        prevRef = currentNode
        currentRef = currentNode.next
        
        # Iterate through the chain and look for the matching key
        # Since they're in ascending order, we can stop looking if we reach > key
        while currentRef is not None and currentRef.key <= key:
            
            # Found the node, remove it
            if currentRef.key == key:
                prevRef.next = currentRef.next
                self.size -= 1
                return currentRef.value
    
            prevRef = currentRef
            currentRef = currentRef.next
    
        # No matching key found
        return defaultValue


    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        return self.size == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        
        return self.size
        
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