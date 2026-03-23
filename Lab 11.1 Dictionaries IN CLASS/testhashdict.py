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
        [2, 7, 12, 13, 24, 38, 43, 44, 52, 61, 73, 74, 85, 97, 102], 
        ['A', 'B', 'E', 'H', 'J', 'K', 'L', 'M', 'P', 'R', 'T', 'W', 'X', 'Y', 'Z']
    )

    print("\n*** TESTING INITIALIZED HASHDICT ***")
    print("\nlen() - expect 15:", len(d))
    print("isEmpty() - expect True:", d.isEmpty())
    print(f"__str__() (uses __iter__())\nExpect keys in order grouped by hash:\n{d}")
    print(f"get(85) - expect X: {d.get(85)}")
    print(f"get(61) - expect A: {d.get(61)}")
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

