# A very simple book class.

class Book:
    
    def __init__(self, title = "", left = None, right = None):
        
        self.title = title
        self.leftChildRef = left
        self.rightChildRef = right