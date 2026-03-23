from linkedlist import LinkedList

def test():

    l = LinkedList()
    print("*** TESTING EMPTY QUEUE ***")
    print("__len__() - expect 0:", len(l))
    print("isEmpty() - expect True:", l.isEmpty())
    print("__str__() - expect nothing:\n\t", l)

    print("*** TESTING INITIALIZED LIST ***")
    l = LinkedList(['one', 'two', 'three'])
    print("__len__() - expect 3:", len(l))
    print("isEmpty() - expect False:", l.isEmpty())
    print("Testing __str__() - expect below:\n\t0. one\n\t1. two\n\t2. three")
    print(f"\n__str__() output (compare above):\n{l}")
    
    l.clear()
    print("Testing insert() - expect below:\n\t0. A\n\t1. B\n\t2. C")
    for i in ['C', 'B', 'A']:
        l.insert(0, i)
    print(f"\ninsert() output (compare above):\n{l}")
    
    print("Testing insert() - expect below:\n\t0. A\n\t1. X\n\t2. B \n\t3. Y\n\t4. C")
    l.insert(1, 'X')
    l.insert(3, 'Y')
    print(f"\ninsert() output (compare above):\n{l}")    

    l = LinkedList(['one', 'two', 'three', 'four', 'five'])
    l.pop()
    l.pop(0)
    l.pop(1)
    print("Testing pop() - expect below:\n\t0: two\n\t1: four")
    print(f"\npop() output (compare above):\n{l}") 
    
    l.pop()
    l.pop()
    print("Testing pop() - expect blank below")
    print(f"\npop() output (compare above):\n{l}") 
    
    l = LinkedList(['one', 'two', 'three', 'four', 'five'])
    print("Testing accessing and assignment with [].")
    l[0] = "AAA"
    l[4] = "YYY"
    print(f"[0] - expect AAA: {l[0]}")
    print(f"[4] - expect YYY: {l[4]}")
    
    l.replace(4, "ZZZ")
    print(f"\nreplace() - expect ZZZ: {l[4]}") 
    
    print(f"\nindex() - expect 4: {l.index('ZZZ')}")    
    
    l = LinkedList(['one', 'two', 'three', 'four', 'five'])
    l.remove('five')
    l.remove('one')
    l.remove('three')
    print("\nTesting remove() - expect below:\n\t0: two\n\t1: four")
    print(f"\nremove() output (compare above):\n{l}")     

if __name__ == "__main__":
    test()