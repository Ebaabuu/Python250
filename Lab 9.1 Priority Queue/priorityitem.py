"""
File: priorityitem.py
"""

class PriorityItem(object):
    """Represents a single item in a priority queue."""

    def __init__(self, priority, data):
        
        if type(priority) != type(1):
            raise ValueError("PriorityItem priority values must be integers.")
            
        # STEP 1
        self.priority = priority
        self.data = data
    
    def __str__(self):
        
        # STEP 2
        return f"[{self.priority}, {self.data}]"

