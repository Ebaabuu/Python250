"""
File: testbag.py
A tester program for bag implementations.
"""

from arraysortedbag import ArraySortedBag

def test():

    print("*** TESTING EMPTY BAG ***")
    b1 = ArraySortedBag()
    print("isEmpty() - expect True:", b1.isEmpty())
    print("__len__() - expect 0:", len(b1))
    print("__str__() - expect {}:", b1)
    print("count(61) - expect 0:", b1.count(61))

    print("\n*** TESTING INITIALIZED BAG ***")
    lyst = [2013, 61, 1973, 42, 1492, 808, 61]
    print("The list of items added is:", lyst)
    b1 = ArraySortedBag(lyst)
    print("__len__() - expect 7:", len(b1))
    print("__str__() - expect {42, 61, 61, 808, 1492, 1973, 2013}:")
    print(f"\t{b1}")
    print("count(61) - expect 2:", b1.count(61))


    b1.remove(2013)
    b1.remove(42)
    b1.remove(808)
    #b1.remove(2013)
    print("remove() - expect {61, 61, 1492, 1973}:", b1)


    b1.add(25)
    b1.remove(25)
    print("add()/remove() - expect {61, 61, 1492, 1973}:", b1)    
       
    b1 = ArraySortedBag([1, 3, 2]) 
    b2 = ArraySortedBag([13, 7]) 
    print("__add__() - expect {1, 2, 3, 7, 13}:", b1 + b2)
    
    # Test large expand and shrink of the array
    b1 = ArraySortedBag()
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
