"""
File: testbst.py

A tester program for binary search trees.
"""

from linkedbst import LinkedBST

def main():
    
    tree = LinkedBST()
    print("*** TESTING EMPTY BST ***")
    print("__len__() - expect 0:", len(tree))
    print("isEmpty() - expect True:", tree.isEmpty())
    print("__str__() - expect blank:\n\t", tree)    
        
    print("*** TESTING INITIALIZED BST ***")
    tree = LinkedBST(["D", "B", "A", "C", "F", "E", "G"])


    print(f"__str__() - see starting list:\n{tree}") 
    print("__len__() - expect  7: ", len(tree))
    print("find(A) - expect  A:", tree.find("A"))
    print("find(X) - expect  None:", tree.find("X"))

    print("\ninorder() - expect A B C D E F G:\n\t", end="")
    for item in tree.inorder(): print(item, end = " ")
    
    print("\npreorder() - expect D B A C F E G:\n\t", end="")
    for item in tree.preorder(): print(item, end = " ")
    
    print("\npostorder() - expect A C B E G F D:\n\t", end="")
    for item in tree.postorder(): print(item, end = " ")
    
    print("\nlevelorder() - expect D B F A C E G:\n\t: ", end="")
    for item in tree.levelorder(): print(item, end = " ")
    
    print("\n__iter__() - expect D B A C F E G:\n\t", end="")
    for item in tree:
        print(item, end=" ")    
    
    print("\nremove() with leaf - expect B C D E F G:\n\t ", end="")
    tree.remove("A")
    for item in tree.inorder(): print(item, end = " ")
       
    print("\nremove() node with 1 child - expect C D E F G:\n\t", end = " ")
    tree.remove("B")    
    for item in tree.inorder(): print(item, end = " ")
    
    print("\nremove() node with 2 children - expect C E F G:\n\t", end = " ")
    tree.remove("D")    
    for item in tree.inorder(): print(item, end = " ")
    
    print("\n\nTesting by adding and removing a lot of items...")
    tree = LinkedBST()
    for i in range(500):
        tree.add(i + 1)
            
    print("__len__() - expect 500:", len(tree))
    for i in range(500, 5, -1):
        tree.remove(i)
    print("__len__() - expect 5:", len(tree))
    print("inorder() - expect 1 2 3 4 5:\n\t", end="")
    for item in tree.inorder(): print(item, end = " ")
    
    for i in range(5):
        tree.remove(i + 1)
    print("\nEmpty with remove() - expect 0:", len(tree))
    
    tree = LinkedBST(["D", "B", "A", "C", "F", "E", "G"])
    tree2 = LinkedBST(["C", "F", "E", "G", "D", "B", "A"])
    tree3 = LinkedBST(["X", "F", "E", "Y", "D", "B", "Z"])
    print(f"__eq__() - expect True: {tree == tree2}")
    print(f"__eq__() - expect False: {tree == tree3}")

    
if __name__ == "__main__":
    main()



