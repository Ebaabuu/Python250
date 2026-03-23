"""
A tester program for queue implementations.
"""

from linkedqueue import LinkedQueue


def test():

    q = LinkedQueue()
    print("*** TESTING EMPTY QUEUE ***")
    print("__len__() - expect 0:", len(q))
    print("isEmpty() - expect True:", q.isEmpty())
    print("__str__() - expect {}:\n\t", q)
    
    print("\n*** TESTING INITIALIZED QUEUE ***")
    print("Add 1-6 via constructor.")
    q = LinkedQueue([i for i in range(1, 7)])
    print("__str__() - expect {1, 2, 3, 4, 5, 6}:\n\t", q)
    print("peek() - expect 1:", q.peek())
    
    print("__len__() - expect 6:", len(q))
    print("isEmpty() - expect False:", q.isEmpty())
    
    print("pop() - expect 1 2 3:", end = " ")
    for count in range(3): print(q.pop(), end = " ")
    print("\n__str__() after pop - expect {4, 5, 6}:\n\t", q)
    
    print("Add 7-9 via add().")
    for i in range(7, 10):
        q.add(i)
        
    print("__str__() - expect {4, 5, 6, 7, 8, 9}:\n\t", q)
    
    print("Make empty with pop().")
    for i in range(len(q)):
        q.pop()
    print("__str__() - expect {}:\n\t", q)
    
    print("__str__() - expect {98, 99}:\n\t", q)
    
    print("\nTesting by adding and removing a lot of items...")
    q = LinkedQueue()
    for i in range(1000):
        q.add(i + 1)
            
    print("__len__() - expect 1000:", len(q))
    for i in range(995):
        q.pop()
    print("__len__() - expect 5:", len(q))
    print("__str__() - expect {996, 997, 998, 999, 1000}:\n\t", q)
    
    print("\n__iter__() - expect 996 997 998 999 1000:\n\t", end="")
    for i in q:
        print(f"{i} ", end="")
    
    q2 = LinkedQueue(['a', 'b', 'c'])
    q3 = LinkedQueue([i for i in range(996, 1001)])
        
    print(f"\n__add__() - expect {{996, 997, 998, 999, 1000, a, b, c}}:\n\t{q + q2}")
    print(f"__eq__() - expect False: {q == q2}")
    print(f"__eq__() - expect True: {q == q3}")
    
    q3.clear()
    print(f"clear() - expect {{}}: {q3}")    

if __name__ == "__main__":
    test()
