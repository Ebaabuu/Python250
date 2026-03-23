"""
File: testheap.py

A tester program for array heaps.
"""

from arrayheap import ArrayHeap

def main():
    heap = ArrayHeap()
    print("Adding 35 78 16 89 54 6 92")
    heap.add(35)
    heap.add(78)
    heap.add(16)
    heap.add(89)
    heap.add(54)
    heap.add(6)
    heap.add(92)
 
    print("\n__str__() - expect 92 89 78 54 35 16 6:\n\t", heap)
    
    print("\npeek() - expect 92:", heap.peek())
    
    print("\nLoop should display contents in descending order: ")
    for item in heap:
        print(item)

    print("\npop() all contents (should display in descending order): ")
    while not heap.isEmpty(): print (heap.pop())
    
    print("\nlen() - expect 0:", len(heap))
    print("__str__() - expect blank:\n", heap)

if __name__ == "__main__":
    main()




