# A very simple book class.

class Book:
    
    def __init__(self, title = "", next = None):
        
        self.title = title
        self.next = next