"""
A tester program for queue implementations.
"""

from priorityitem import PriorityItem
from priorityqueue import PriorityQueue


def test():
    
    # Make some priority items to test with
    i1 = PriorityItem(1, "one")
    i2 = PriorityItem(2, "two")
    i3 = PriorityItem(3, "three")
    i4 = PriorityItem(4, "four")
    i5 = PriorityItem(5, "five")
    i6 = PriorityItem(1, "another one")
    i7 = PriorityItem(3, "another three")
    i8 = PriorityItem(5, "another five")
    
    itemList = [i1, i2, i3, i4, i5, i6, i7]
        
    q = PriorityQueue()
    print("*** TESTING EMPTY QUEUE ***")
    print("__len__() - expect 0:", len(q))
    print("isEmpty() - expect True:", q.isEmpty())
    print("__str__() - expect {}:\n", q)
    
    print("\n*** TESTING INITIALIZED QUEUE ***")
    q = PriorityQueue(itemList)
    print(f"\n__str__() - expect below\n\t[1, another one]\n\t[1, one]\n\t[2, two]\n\t[3, another three]\n\t[3, three]\n\t[4, four]\n\t[5, five]\n\t:")
    print(f"\n__str__() output (compare above):\n{q}")
    print("peek() - expect [1, another one]:", q.peek())
    
    print("__len__() - expect 7:", len(q))
    print("isEmpty() - expect False:", q.isEmpty())
    
    print("pop() - expect [1, another one] [1, one] [2, two]:", end = " ")
    for count in range(3): print(q.pop(), end = " ")
    
    print(f"\nAfter pop()s - expect below\n\t[3, another three]\n\t[3, three]\n\t[4, four]\n\t[5, five]:")
    print(f"\nAfter pop()s output (compare above):\n{q}")    

    print("Make empty with pop().")
    while not q.isEmpty():
        q.pop()
    print("__str__() - expect blank:\n\t", q)
    
    q = PriorityQueue([i2, i4, i6, i8])
    q2 = PriorityQueue([i1, i3, i5, i7])
    q3 = PriorityQueue([i2, i4, i6, i8])
        
    print(f"\n__add__() - expect below\n\t[1, another one]\n\t[1, one]\n\t[2, two]\n\t[3, another three]\n\t[3, three]\n\t[4, four]\n\t[5, five]\n\t[5, another five]:")
    print(f"\n__add__() output (compare above):\n{q2 + q3}")
    print(f"__eq__() - expect False: {q == q2}")
    print(f"__eq__() - expect True: {q == q3}")
    
    #q3.clear()
    #print(f"clear() - expect {{}}: {q3}")    

if __name__ == "__main__":
    test()
