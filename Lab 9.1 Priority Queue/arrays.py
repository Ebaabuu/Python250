"""
File: arrays.py

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.__items = list()
        for count in range(capacity):
            self.__items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.__items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.__items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self.__items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""

        """Python is tricky. Slicing automatically works with anything
        that is subscriptable unless we disable it. This disables it.
        Attempting to use slicing with an array results in an exception."""
        if isinstance(index, slice):
            raise TypeError("Array does not support slicing.")

        return self.__items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.__items[index] = newItem
