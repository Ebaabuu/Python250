"""
File: node.py
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


