"""
File: entry.py
"""

class Entry(object):
    """Represents a dictionary entry."""

    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

