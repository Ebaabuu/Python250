from bookpile import BookPile

def main():
    
    print("*** TESTING EMPTY PILE ***")
    print("You'll need to verify that the output is correct manually.")
    b1 = BookPile()
    
    print("\nTest isEmpty()")
    print(b1.isEmpty())
    
    print("\nTest len()")
    print(len(b1))
    
    print("\nTest __str__()")
    print(b1)    
    
    print("\n*** TESTING INITIALIZED PILE ***")
    books = [ "Dune", "Dragonflight", "Neuromancers", "Contact",
              "Brave New World", "Cinder", "Rust", "Random1ze",  "Sea of Rust",
              "Brave New World", "Emma", "Cinder", "Rust", "Random1ze",  "Sea of Rust",
              "All Systems Red", "Jaws"]    
    
    myPile = BookPile(books)
    
    print("\nTest isEmpty()")
    print(myPile.isEmpty())    
    
    print("\nTest __str__()")
    print(myPile)
    
    print("\nTest len()")
    print(len(myPile))
    
    print("\nTest addBook()")
    print(myPile.addBook("The Fellowship of the Ring"))
    print(myPile)
    
    print("\nTest addBook()")
    print(myPile.addBook("The Fellowship of the Ring"))
    print(myPile)    
    
    print("\nTest __iter__()")
    myPile = BookPile(books)    
    for i in myPile:
        print(i)
    
    myPile = BookPile(books)
    print(f"\nCurrent pile:\n{myPile}")
    print("\nTest contains()")
    print(myPile.contains("All Systems Red"))
    print(myPile.contains("Dragonflight"))
    print(myPile.contains("Dune"))
    print(myPile.contains("123456"))
    
    print("\nTest bookPosition()")
    print(myPile.bookPosition("All Systems Red"))
    print(myPile.bookPosition("Neuromancer"))
    print(myPile.bookPosition("Dune"))
    print(myPile.bookPosition("12345"))
        
    print("\nTest __getitem__()")
    print(myPile[1])
    print(myPile[5])
    print(myPile[10])

    print()
    #print(myPile.tempPrinter())
    """
    
    print(f"\nCurrent pile:\n{myPile}")
    print("\nTest removeBook()")
    print("Pile Before:")
    print(myPile)
    print(myPile.removeBook("All Systems Red"))
    print(myPile.removeBook("Neuromancers"))
    print(myPile.removeBook("Dune"))
    print(myPile.removeBook("12345"))
    print(f"\nPile after removeBook():\n{myPile}")
    print(f"\nCount after removeBook():\n{len(myPile)}")

    
    myPile = BookPile(books)
    print(f"\nCurrent pile:\n{myPile}")
    print("\nTest removePosition()")
    print(myPile.removePosition(20))
    print(myPile.removePosition(12))
    print(myPile.removePosition(10))
    print(myPile.removePosition(5))
    print(myPile.removePosition(1))
    print(f"\nPile after removePosition():\n{myPile}")
    print(f"\nCount after removePosition():\n{len(myPile)}")
    
    myPile = BookPile(books)
    print(f"\nCurrent pile:\n{myPile}")
    print("\nTest rename()")
    print(myPile.rename("Rust", "More Rust"))
    print(myPile.rename("Bob", "More Bob"))
    print(myPile.rename("Dragonflight", "Dragon"))
    print(myPile.rename("All Systems Red", "Brave New World"))
    print(f"\nPile after rename():\n{myPile}")
    print(f"\nCount after rename():\n{len(myPile)}")
    
    myPile = BookPile(books)
    print("\nTest clear()")
    myPile = BookPile(books) 
    myPile.clear()
    print(f"\nPile after clear():\n{myPile}")
    
    print("\nTest __eq__()")
    myPile = BookPile(books) 
    otherPile = BookPile(books)
    pile3 = BookPile(["A", "BB", "CCC"])
    pile4 = BookPile(["A", "B", "C"])
    print(myPile == myPile)
    print(myPile == books)
    print(myPile == otherPile)
    print(myPile == pile3)
    print(pile3 == pile4)
    print()

    myPile = BookPile(books)
    print(myPile.tempPrinter())

    print()"""

    print("REMOVE TESTING")
    myPile = BookPile(books)
    print(myPile)
    for item in myPile:
        myPile.removeBook(item)

    print(myPile)

    print("\nBig add/remove test")
    myPile = BookPile()
    for i in range(100):
        myPile.addBook(str(i))
    while not myPile.isEmpty():
        myPile.removePosition(1)
    print(f"\nPile after big add/remove:\n{myPile}")
    print(f"\nCount after big add/remove:\n{len(myPile)}")

    print()
    print()

    books = ["Laiyla", "The Land", "Awaken Online", "Dungeon Born", "He Who Fights with Monsters", "Ready Player One",
             "Dungeon Crawler Carl", "Cradle", "Dungeon Crawler Carl", "Awaken Online"]
    myPile = BookPile(books)

    print("RENAME")
    print("Dungeon Crawler Carl", "Dungeon Crawler Carl and Princess Donut")
    print(myPile.rename("Dungeon Crawler Carl", "Dungeon Crawler Carl and Princess Donut"))
    print(myPile.size)
    print("The Land", "The Land: Origins")
    print(myPile.rename("The Land", "The Land: Origins"))
    print(myPile.size)
    print("Dungeon Born", "Some Different Title")
    print(myPile.rename("Dungeon Born", "Some Different Title"))
    print(myPile.size)
    print("Awaken Online", "Cradle")
    print(myPile.rename("Awaken Online", "Cradle"))
    print(myPile.size)
    print(myPile)
    print(len(myPile))
    
if __name__ == "__main__":
    main()
    