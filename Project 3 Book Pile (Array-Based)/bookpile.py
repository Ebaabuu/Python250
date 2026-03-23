"""
@author Emaad Gafoor
file: bookpile.py
"""
from arrays import Array

class BookPile:
    """
    Bookpile object represents a pile of books ordered into an array
based on length, with longer names placed first.

    Member Variables:
        books(array):
        size(int):
    """
    # Class variable representing the default size capacity
    DEFAULT_CAPACITY = 4

    def __init__(self, sourceCollection = None):
        # Call clear() to innitialize empty array with default capacity
        self.clear()

        # Add items from given source
        if sourceCollection:
            for item in sourceCollection:
                self.addBook(item)

    def __len__(self):
        return self.size

    def __getitem__(self, position):
        # Check for invalid position
        if position > len(self) or position < 1:
            raise IndexError("ERROR: Invalid position.")

        return self.books[position - 1]

    def __eq__(self, other):
        if self is other: # Same reference location
            return True

        if type(self) != type(other): # Differing types
            return False

        if self.size != other.size: # Differing logical sizes
            return False

        # Iterate until differing value located
        for item in self:
            if not item in other:
                return False

        return True

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.books[cursor]
            cursor += 1

    def __str__(self):
        counter = 1

        if len(self) > 0:
            bookString = ""
            for item in self:
                bookString += f"{counter}. {item} ({len(item)})\n"
                counter += 1
            bookString = bookString.rstrip()

            return bookString
        else:
            return "Book pile is empty."

    def clear(self):
        """
            clear() creates a new array with the default capacity and
        points the books member variable to the new array. Size is
        set to 0 for the empty array.
        """
        self.books = Array(BookPile.DEFAULT_CAPACITY)
        self.size = 0

    def addBook(self, book):
        """
            addBook() adds a given book from parameter book into the books
        member variable array. The new book must have a title with at least
        one character and no repeats.

            Parameters:
                book (string): Name of book being inserted

            Returns:
                bool: True if book is added, else False
        """
        # Must have at least one character in book title
        if len(book) < 1:
            return False

        # Can't repeat book titles
        if self.contains(book):
            return False

        # Readjust physical size if array is full
        if self.size == len(self.books):
            tempArray = Array(2 * len(self))

            for i in range(len(self)):
                tempArray[i] = self.books[i]
            self.books = tempArray

        # Find index where book will be placed in array
        indexToAdd = 0
        for i in range(len(self)):
            if len(book) < len(self.books[i]):
                indexToAdd += 1

        # Make space for new book by moving books with shorter titles
        # further in the array
        for i in range(self.size, indexToAdd, -1):
            self.books[i] = self.books[i - 1]
        self.books[indexToAdd] = book

        self.size += 1
        return True

    def removeBook(self, title):
        """
            removeBook() removes a specified book from the books array
        dependent on the given book title.

            Parameters:
                title (string): name of book being removed

            Return:
                bool: True if book is successfully removed, else False
        """
        # Check to see if book is in collection
        if not self.contains(title):
            return False

        # Decrement Array until title is reached to overwrite
        # the title
        indexToRemove = self.bookPosition(title) - 1
        for i in range(indexToRemove, self.size):
            self.books[i] = self.books[i + 1]
        self.size -= 1

        # Readjust physical array size if logical size becomes too small
        if self.size <= (len(self.books) // 4):
            if self.DEFAULT_CAPACITY > len(self.books) // 2:
                newSize = self.DEFAULT_CAPACITY
            else:
                newSize = len(self.books) // 2

            temp = Array(newSize)
            for i in range(self.size):
                temp[i] = self.books[i]
            self.books = temp

        return True

    def removePosition(self, position):
        """
            removePosition() removes the book at the given position.

            Parameters:
                position (int): position of item to remove (index + 1)

            Return:
                bool: True if successful, else False
        """
        # Test for valid position and short circuit if false
        if (self.size >= position > 0 and
                self.removeBook(self.books[position - 1])):
            return True
        return False

    def isEmpty(self):
        """
            isEmpty() checks if the books array is logically empty

            Returns:
                bool: True if successful, else False
        """
        if self.size == 0:
            return True
        return False

    def contains(self, title):
        """
            isEmpty() checks if the books array contains the given title

            Returns:
                bool: True if successful, else False
        """
        for book in self:
            if book == title:
                return True
        return False

    def bookPosition(self, title):
        """
            bookPosition() gives the index of the given title + 1

            Parameters:
                title (string): name of book to find position of

            Returns:
                int: position of given book, -1 if not found
        """
        counter = 1
        for item in self:
            if title == item:
                return counter
            counter += 1
        return -1

    def rename(self, oldName, newName):
        """
            rename() takes a given name and changes it to a new given name.
        Old name is removed and new name is added to preserve correct order.

            Parameters:
                oldName (string): Name to be removed
                newName (string): Name to be added

            Returns:
                bool: True if successful, else False
        """
        # Remove old name and add new name to keep
        # order maintained
        if self.contains(oldName) and not self.contains(newName):
            self.removeBook(oldName)
            self.addBook(newName)
            return True
        return False
