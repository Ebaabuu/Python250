"""
File: testbag.py
A tester program for bag implementations.
"""

from arraybag import ArrayBag

def test():
    
    print("*** TESTING EMPTY BAG ***")
    b1 = ArrayBag()
    print("isEmpty() - expect True:", b1.isEmpty())
    print("__len__() - expect 0:", len(b1))
    print("__str__() - expect {}:", b1)
    print("count(61) - expect 0:", b1.count(61))
    
    
    print("\n*** TESTING INITIALIZED BAG ***")
    lyst = [2013, 61, 1973, 42, 1492, 808, 61]
    print("The list of items added is:", lyst)
    b1 = ArrayBag(lyst)
    print("__len__() - expect 7:", len(b1))
    print("__str__() - expect {2013, 61, 1973, 42, 1492, 808, 61}:")
    print(f"\t{b1}")
    print("count(61) - expect 2:", b1.count(61))
    
    for item in lyst:
        b1.remove(item)
    print("remove() - expect {}:", b1)    
    
    b1 = ArrayBag(lyst)
    b1.clear()
    print("clear() - expect {}:", b1)
    
    b1.add(25)
    b1.remove(25)
    print("add()/remove() - expect {}:", b1)
   
    b1 = ArrayBag(lyst)
    b2 = ArrayBag([2013, 1492, 808, 61, 61, 1973, 42])
    b3 = ArrayBag([2013, 61, 1973])
    b4 = ArrayBag([2013, 2013, 2013, 2013, 2013, 2013, 2013])
    print("__eq__() - expect True:", b1 == b2)
    print("__eq__() - expect False:", b1 == b3)
    print("__eq__() - expect False:", b1 == b4)
    
    b1 = ArrayBag([1, 2, 3]) 
    b2 = ArrayBag([7, 13]) 
    print("__add__() - expect {1, 2, 3, 7, 13}:", b1 + b2)
    
    # Test large expand and shrink of the array
    b1 = ArrayBag()
    for i in range(1, 1001):
        b1.add(i)
    print("__len__() - expect 1000:", len(b1))
    for i in range(5, 1001):
        b1.remove(i) 
    print("add()/remove() - expect {1, 2, 3, 4}:", b1)
    
    print("Expect crash with KeyError exception:")
    
    try:
        b2.remove(99)
        
    except KeyError as e:
        
        print(f"\tException caught, error message: {e}")

if __name__ == "__main__":
    test()
