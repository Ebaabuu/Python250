class Shape:
    def __init__(self, name = "Generic Shape", color = "black"):
        self.name = name
        self.color = color
        
    def printName(self):
        print(f"The name of the shape is {self.name}.")
        
    def printColor(self):
        print(f"The color of {self.name} is {self.color}.")    
        
    def printArea(self):
        print(f"{self.name} does not have an area.")
    
    def printPerimeter(self):
        print(f"{self.name} does not have a perimeter.")    