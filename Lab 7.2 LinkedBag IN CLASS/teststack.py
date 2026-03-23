from linkedstack import LinkedStack

def test():

    print("*** TESTING EMPTY STACK ***")
    b1 = LinkedStack()
    print("isEmpty() - expect True:", b1.isEmpty())
    print("__len__() - expect 0:", len(b1))
    print("__str__() - expect {}:", b1)
    
    print("\n*** TESTING INITIALIZED STACK ***")
    lyst = [2013, 61, 1973, 42, 1492, 808, 61]
    print("The list of items pushed is:", lyst)
    b1 = LinkedStack(lyst)
    print("__len__() - expect 7:", len(b1))
    print("__str__() - expect {2013, 61, 1973, 42, 1492, 808, 61}:")
    print(f"\t{b1}")
    print(f"peek() - expect 61: {b1.peek()}")

    for item in lyst:
        b1.pop()
    print("pop() - expect {}:", b1)    
    
    b1 = LinkedStack(lyst)
    b1.clear()
    print("clear() - expect {}:", b1)
    
    b1.push(25)
    print(f"pop() - expect 25: {b1.pop()}")
    print("push()/pop() - expect {}:", b1)
   
    b1 = LinkedStack([2013, 1492, 808, 61, 61, 1973, 42])
    b2 = LinkedStack([2013, 1492, 808, 61, 61, 1973, 42])
    b3 = LinkedStack([2013, 61, 1973])
    b4 = LinkedStack([2013, 2013, 2013, 2013, 2013, 2013, 2013])
    print("__eq__() - expect True:", b1 == b1)
    print("__eq__() - expect True:", b1 == b2)
    print("__eq__() - expect False:", b1 == b3)
    print("__eq__() - expect False:", b1 == b4)
    
    b1 = LinkedStack([1, 2, 3]) 
    b2 = LinkedStack([7, 13]) 
    print("__add__() - expect {1, 2, 3, 7, 13}:", b1 + b2)
    
    # Test large expand and shrink of the chain
    b1 = LinkedStack()
    for i in range(1, 1001):
        b1.push(i)
    print("__len__() - expect 1000:", len(b1))
    for i in range(5, 1001):
        b1.pop() 
    print("push()/pop() - expect {1, 2, 3, 4}:", b1)
    
    # Test iterator
    b1 = LinkedStack(lyst)
    print("__iter__() - expect 2013 (bottom) first and 61 (top) last:")
    for i in b1:
        print(i)
    
    # Test pop exception
    b2.clear()
    
    print("Expect crash with KeyError exception from pop():")
    
    try:
        b2.pop()
        
    except KeyError as e:
        
        print(f"\tException caught, error message: {e}")

if __name__ == "__main__":
    test()