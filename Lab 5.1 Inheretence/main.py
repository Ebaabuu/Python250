from shape import Shape
from rectangle import Rectangle

def main():
    
    print("*** SHAPE TESTS ***")
    s = Shape("Shape Bob", "blue")
    s.printName()
    s.printColor()
    s.printArea()
    s.printPerimeter()
    
    print("\n*** DEFAULT RECTANGLE TESTS ***")
    r = Rectangle()
    
    print("*Below should be 'The name of the shape is Generic Rectangle.'")
    r.printName()
    
    print("\n*Below should be 'The color of Generic Rectangle is green.'")
    r.printColor()
    
    print("\n*Below should be 'Generic Rectangle has an area of 1.'")
    r.printArea()
    
    print("\n*Below should be 'Generic Rectangle has a perimeter of 4.'")
    r.printPerimeter()     
    
    print("\n*** RECTANGLE TESTS ***")
    r = Rectangle(10, 10, "Rectangle James", "red")
    
    print("*Below should be 'The name of the shape is Rectangle James.'")
    r.printName()
    
    print("\n*Below should be 'The color of Rectangle James is red.'")
    r.printColor()
    
    print("\n*Below should be 'Rectangle James has an area of 100.'")
    r.printArea()
    
    print("\n*Below should be 'Rectangle James has a perimeter of 40.'")
    r.printPerimeter()    
    
if __name__ == "__main__":
    main()