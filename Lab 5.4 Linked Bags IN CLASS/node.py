"""
File: node.py
"""

class Node(object):
    """Represents a single node in a linked chain."""

    def __init__(self, data, next = None):

        self.data = data
        self.next = next