"""
File: Dictinterface.py
"""

class DictInterface(object):
    """Interface for all dictionaries."""

    # Constructor
    def __init__(self, keys = None, values = None):
        """Will copy entries to the dictionary
        from keys and values if they are present."""
        pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return True
    
    def __len__(self):
        """Returns the number of items in self."""
        return 0

    def __str__(self):
        """Returns the string representation of self."""
        return ""

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        return None

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return False

    def get(self, key, defaultValue = None):
        """Returns the associated value if the key in in the
        dictionary, or returns the default value otherwise."""
        
        return defaultValue
   
    def __add__(self, otherDict):
        """Returns a dictionary containing the items of self and
        otherDict.  When keys are equal, the value in otherDict replaces
        the value in self."""
        return type(self)()

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value 
        if the key is in the dictionary,
        or returns the default value otherwise."""
        return None
    
    # Returns the hash index of the given key for a table of 
    # tableSize. Assumes key is an integer.
    def __hash(self, key, tableSize):
        
        pass


