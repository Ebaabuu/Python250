"""
File: testhashdict.py
A program for testing rehasing of a hash dictionary.
"""

from hashdict import HashDict

def main():
    
    d = HashDict()
    
    print("*** TESTING EMPTY HASHDICT ***")
    print("__len__() - expect 0:", len(d))
    print("isEmpty() - expect True:", d.isEmpty())
    print("__str__() - expect blank:\n", d)     
    
    d = HashDict(
        [2, 7, 12, 13, 24, 38, 43, 44, 52, 73, 74, 85], 
        ['A', 'B', 'E', 'H', 'J', 'K', 'L', 'M', 'P', 'T', 'W', 'X']
    )

    print("\n*** TESTING INITIALIZED HASHDICT ***")
    print("\nlen() - expect 12:", len(d))
    print("isEmpty() - expect True:", d.isEmpty())
    print(f"__str__():\n{d}")
    print(f"contains(85) - expect True: {d.contains(85, 'X')}")
    print(f"contains(7) - expect True: {d.contains(7, 'B')}")
    print(f"contains(85) - expect False: {d.contains(85, 'A')}")
    print(f"contains(7) - expect False: {d.contains(7, 'Z')}") 
    print(f"contains(85) - expect False: {d.contains(75, 'X')}")
    print(f"contains(7) - expect False: {d.contains(77, 'B')}")    
  
    d2 = HashDict(
        [2, 7, 12, 13, 24, 38, 43, 44, 52, 73, 74, 85], 
        ['A', 'B', 'E', 'H', 'J', 'K', 'L', 'M', 'P', 'T', 'W', 'X']
    )
    d3 = HashDict(
        [2, 7, 12, 13, 24, 38, 43, 44], 
        ['A', 'B', 'E', 'H', 'J', 'K', 'L', 'M']
    )
    d4 = HashDict(
        [2, 7, 12, 13, 24, 38, 43, 44, 52, 73, 74, 86], 
        ['A', 'B', 'E', 'H', 'J', 'K', 'L', 'M', 'P', 'T', 'W', 'X']
    )    
    d5 = HashDict(
        [2, 7, 12, 13, 24, 38, 43, 44, 52, 73, 74, 85], 
        ['A', 'B', 'E', 'H', 'J', 'K', 'L', 'M', 'P', 'T', 'W', 'X'],
        20
    )    
    
    print(f"\nd == d2 - expect True: {d == d2}")
    print(f"\nd == d5 - expect True: {d == d5}")
    print(f"d == d3 - expect False: {d == d3}")
    print(f"d == d4 - expect False: {d == d4}")
    print(f"d == list - expect False: {d == ['A', 'B']}")
    
    print(f"\nget(85) - expect X: {d.get(85)}")
    print(f"get(61) - expect None: {d.get(61)}")
    print(f"get(7) - expect B: {d.get(7)}")
    print(f"get(38) - expect K: {d.get(38)}")
    print(f"get(74) - expect W: {d.get(74)}")
    print(f"get(99) - expect None: {d.get(99)}")
    
    print(f"\npop(85) - expect X: {d.pop(85)}")
    print(f"pop(61) - expect A: {d.pop(61)}")
    print(f"pop(7) - expect B: {d.pop(7)}")
    print(f"pop(38) - expect K: {d.pop(38)}")
    print(f"pop(74) - expect W: {d.pop(74)}")
    
    print(f"pop(99) - expect None: {d.pop(99)}")    
    
if __name__ == "__main__":
    main()

