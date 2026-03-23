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
              "Brave New World", "Cinder", "Rust", "Random1ze",  "Sea of Rust",
              "All Systems Red"]    
    
    myPile = BookPile(books)
    
    print("\nTest isEmpty()")
    print(myPile.isEmpty())    
    
    print("\nTest __str__()")
    print(myPile)
    
    print("\nTest len()")
    print(len(myPile))

    print("\nTest []")
    print(myPile[5])
    
    print("\nTest addBook()")
    print(myPile.addBook("The Fellowship of the Ring"))
    print(myPile)
    
    print("\nTest addBook()")
    print(myPile.addBook("The Fellowship of the Ring"))
    print(myPile)    
        
    print("\nTest contains()")
    myPile = BookPile(books)
    print(myPile.contains("All Systems Red"))
    print(myPile.contains("Dragonflight"))
    print(myPile.contains("Dune"))
    print(myPile.contains("123456"))  
    
    print("\nTest bookPosition()")
    print(myPile)
    print(myPile.bookPosition("All Systems Red"))
    print(myPile.bookPosition("Neuromancers"))
    print(myPile.bookPosition("Dune"))
    print(myPile.bookPosition("12345"))
        
    print("\nTest __getitem__()")
    print(myPile[1])
    print(myPile[5])
    print(myPile[10])
    
    print("\nTest removeBook()")
    print(myPile.removeBook("All Systems Red"))
    print(myPile.removeBook("Neuromancers"))
    print(myPile.removeBook("Dune"))
    print(myPile.removeBook("12345"))
    print(myPile)
    
    print("\nTest removePosition()")
    myPile = BookPile(books)
    print(myPile.removePosition(1))
    print(myPile.removePosition(5))
    print(myPile.removePosition(10))
    print(myPile.removePosition(12))
    print(myPile)
    
    print("\nTest __iter__()")
    myPile = BookPile(books)    
    for i in myPile:
        print(i)
    
    print("\nTest rename()")
    myPile = BookPile(books) 
    print(myPile.rename("Rust", "More Rust"))
    print(myPile.rename("Dragonflight", "Dragon"))
    print(myPile)
    
    print("\nTest rename()")
    myPile = BookPile(books) 
    print(myPile.rename("Bob", "More Bob"))
    print(myPile)
    
    print("\nTest clear()")
    myPile = BookPile(books) 
    myPile.clear()
    print(myPile)    
    
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
    
    print("\nBig add/remove test")
    myPile = BookPile()
    for i in range(1000):
        myPile.addBook(str(i))
    while not myPile.isEmpty():
        myPile.removePosition(1)
    print(myPile)
    
if __name__ == "__main__":
    main()
    