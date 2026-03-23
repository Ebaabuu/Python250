"""
File: testbag.py
A tester program for bag implementations.
"""

from linkedbag import LinkedBag

def test():
    
    print("*** TESTING EMPTY BAG ***")
    b1 = LinkedBag()
    print("isEmpty() - expect True:", b1.isEmpty())
    print("__len__() - expect 0:", len(b1))
    print("__str__() - expect {}:", b1)
    print("count(61) - expect 0:", b1.count(61))
    
    
    print("\n*** TESTING INITIALIZED BAG ***")
    lyst = [1, 2, 3, 3, 4, 5, 6]
    print("The list of items added is:", lyst)
    b1 = LinkedBag(lyst)
    print("__len__() - expect 7:", len(b1))
    print("__str__() - expect {1, 2, 3, 3, 4, 5, 6}:")
    print(f"\t{b1}")
    print("count(3) - expect 2:", b1.count(3))

    print(b1)
    
    b1.remove(1)
    b1.remove(6)
    for item in [2, 3, 3, 4, 5]:
        b1.remove(item)
    print("remove() - expect {}:", b1)    
    
    b1 = LinkedBag(lyst)
    b1.clear()
    print("clear() - expect {}:", b1)
    
    b1.add(25)
    b1.remove(25)
    print("add()/remove() - expect {}:", b1)
   
    # Test large expand and shrink of the array
    b1 = LinkedBag()
    for i in range(1, 1001):
        b1.add(i)
    print("__len__() - expect 1000:", len(b1))
    for i in range(5, 1001):
        b1.remove(i) 
    print("add()/remove() - expect {1, 2, 3, 4}:", b1)


if __name__ == "__main__":
    test()
