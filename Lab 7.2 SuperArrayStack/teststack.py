from superarraystack import SuperArrayStack

def test():
    
    # Test index access
    s1 = SuperArrayStack([2013, 1492, 808, 61, 1973, 42])

    print(f"s1[0] - expect 42: {s1[0]}")
    print(f"s1[3] - expect 808: {s1[3]}")
    print(f"s1[5] - expect 2013: {s1[5]}")
    
    # Test index assignment
    s1[0] = "top"
    s1[3] = "mid"
    s1[5] = "bottom"
    print("\n__str__() - expect {bottom, 1492, mid, 61, 1973, top}:")
    print(f"\t{s1}")

    '''#index test
    print()
    s1.indexTest()
    print()'''

    # Test insert()
    s1 = SuperArrayStack([808, 61, 1973, 42])
    s1.insert(0, 99)
    print("\ninsert() - expect {808, 61, 1973, 42, 99}:")
    print(f"\t{s1}")   
    s1 = SuperArrayStack([808, 61, 1973, 42])
    s1.insert(3, 99)
    print("insert() - expect {808, 99, 61, 1973, 42}:")
    print(f"\t{s1}")
    s1 = SuperArrayStack([808, 61, 1973, 42])
    s1.insert(4, 99)
    print("insert() - expect {99, 808, 61, 1973, 42}:")
    print(f"\t{s1}")

    
    # Test remove()
    s1 = SuperArrayStack([808, 61, 808, 1973, 42])
    print(f"\nremove() - expect True: {s1.remove(808)}")
    print(f"remove() - expect True: {s1.remove(808)}")
    print(f"remove() - expect False: {s1.remove(808)}")
    print("After remove() - expect {61, 1973, 42}:")
    print(f"\t{s1}")        
    
    # Test sort()
    s1 = SuperArrayStack([42, 1492, 808, 2013, 1973, 61])
    s1.sort()
    print("\nsort() - expect {2013, 1973, 1492, 808, 61, 42}:")
    print(f"\t{s1}") 
    
    print("\nExpect crash with KeyError exception from insert():")
    
    try:
        s1 = SuperArrayStack([42, 1492, 808, 2013, 1973, 61])
        s1.insert(10, 99)
        
    except KeyError as e:
        
        print(f"\tException caught, error message: {e}")
        
    # Uncomment below to test functionality 
    # inherited from ArrayStack.

    '''
    print("*** TESTING EMPTY STACK ***")
    b1 = SuperArrayStack()
    print("isEmpty() - expect True:", b1.isEmpty())
    print("__len__() - expect 0:", len(b1))
    print("__str__() - expect {}:", b1)
    
    print("\n*** TESTING INITIALIZED STACK ***")
    lyst = [2013, 61, 1973, 42, 1492, 808, 61]
    print("The list of items pushed is:", lyst)
    b1 = SuperArrayStack(lyst)
    print("__len__() - expect 7:", len(b1))
    print("__str__() - expect {2013, 61, 1973, 42, 1492, 808, 61}:")
    print(f"\t{b1}")
    
    for item in lyst:
        b1.pop()
    print("pop() - expect {}:", b1)    
    
    b1 = SuperArrayStack(lyst)
    b1.clear()
    print("clear() - expect {}:", b1)
    
    b1.push(25)
    print(f"pop() - expect 25: {b1.pop()}")
    print("push()/pop() - expect {}:", b1)
   
    b1 = SuperArrayStack([2013, 1492, 808, 61, 61, 1973, 42])
    b2 = SuperArrayStack([2013, 1492, 808, 61, 61, 1973, 42])
    b3 = SuperArrayStack([2013, 61, 1973])
    b4 = SuperArrayStack([2013, 2013, 2013, 2013, 2013, 2013, 2013])
    print("__eq__() - expect True:", b1 == b2)
    print("__eq__() - expect False:", b1 == b3)
    print("__eq__() - expect False:", b1 == b4)
    
    b1 = SuperArrayStack([1, 2, 3]) 
    b2 = SuperArrayStack([7, 13]) 
    print("__add__() - expect {1, 2, 3, 7, 13}:", b1 + b2)
    
    # Test large expand and shrink of the array
    b1 = SuperArrayStack()
    for i in range(1, 1001):
        b1.push(i)
    print("__len__() - expect 1000:", len(b1))
    for i in range(5, 1001):
        b1.pop() 
    print("push()/pop() - expect {1, 2, 3, 4}:", b1)
    '''    

if __name__ == "__main__":
    test()