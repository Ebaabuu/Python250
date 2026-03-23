from shape import Shape

class Rectangle(Shape):
    def __init__(self, width = 1, height = 1, name = "Generic Rectangle", color = "green"):
        self.width = width
        self.height = height
        self.name = name
        self.color = color

    def printArea(self):
        print(f"{self.name} has an area of {self.width * self.height}.")

    def printPerimeter(self):
        print(f"{self.name} has a perimeter of {self.width * 2 + self.height * 2}.")