"""
@author Emaad Gafoor
file: bookpile.py
"""
from book import Book
class BookPile:
    """
        Bookpile object represents a pile of books ordered into a linked chain
    based on title length, with longer names placed first.

        Member Variables:
            head(book): Reference to first book in the chain
            size(int): Number of books in pile
        """

    def __init__(self,  sourceCollection = None):
        # Call clear() to initialize empty array with default capacity
        self.clear()

        # Add items from given source
        if sourceCollection:
            for item in sourceCollection:
                self.addBook(item)

    def __len__(self):
        return self.size

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""

        # Are they the same object?
        if self is other:
            return True

        # Are they the different types?
        if type(self) != type(other):
            return False

        # Do they contain a different number of items?
        if len(self) != len(other):
            return False

        # Do they contain the same items?
        for item in self:
            if item not in other:
                return False

        return True

    def __iter__(self):
        """Supports iteration over each book title in linked chain"""
        cursor = self.head
        while cursor is not None:
            yield cursor.title
            cursor = cursor.next

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

    def __getitem__(self, position):
        if position < 1 or position > self.size:
            raise IndexError("ERROR: Invalid position.")
        curNode = self.head
        counter = 1
        while curNode is not None:
            # Iterate until the given position is reached and return
            # title at position
            if counter == position:
                return curNode.title
            curNode = curNode.next
            counter += 1

    def addBook(self, title):
        """
            addBook() adds a given book from parameter book into the bookpile
        linked chain. The new book must have a title with at least one character
        and no repeats.

            Parameters:
                title (string): Name of book being inserted

            Returns:
                bool: True if book is added, else False
        """
        # Must have at least one character in book title
        if len(title) < 1:
            return False

        # Can't repeat book titles
        if self.contains(title):
            return False

        # Create new book with given title
        newNode = Book(title)

        # Check if Bookpile is empty and place the new book at the
        # beginning
        if self.head is None:
            self.head = newNode
        # Check if the given title is longer than first book's title
        # and place it at the beginning
        elif len(title) >= len(self.head.title):
            newNode.next = self.head
            self.head = newNode
        else:
            found = False
            curNode = self.head
            while not found:
                # If the next node is none, then the final node has
                # been reached. Place new node at the end.
                if curNode.next is None:
                    curNode.next = newNode
                    found = True
                # Find the last node that is larger than the new node
                # (curNode) and place the new node after that
                elif len(newNode.title) >= len(curNode.next.title):
                    newNode.next = curNode.next
                    curNode.next = newNode
                    found = True
                curNode = curNode.next

        self.size += 1
        return True

    def bookPosition(self, title):
        """
            bookPosition() gives the position of the given title within the
        linked chain

            Parameters:
                title (string): name of book to find position of

            Returns:
                int: position of given book, -1 if not found
        """
        counter = 1
        for book in self:
            if title == book:
                return counter
            counter += 1
        return -1

    def isEmpty(self):
        """
            isEmpty() checks if the linked chain has any books.

            Returns:
                bool: True if successful, else False
        """
        if self.size == 0:
            return True
        return False

    def clear(self):
        """
            clear() points head at None to remove all items in the linked
        chain. size is set to zero.
        """
        self.head = None
        self.size = 0

    def contains(self, title):
        """
            contains() iterates through the linked chain until the given title
        is found in the chain or chain is fully traversed.

            Returns:
                bool: True if successful, else False
        """
        for book in self:
            if book == title:
                return True
        return False

    def removeBook(self, title):
        """
            removeBook() removes a specified book from the linked chain
        dependent on the given book title.

            Parameters:
                title (string): name of book being removed

            Return:
                bool: True if book is successfully removed, else False
        """
        # Check if pile is empty
        if self.isEmpty():
            return False

        # Check if the first book is the one to be removed
        elif self.head.title == title:
            self.head = self.head.next
            self.size -= 1
            return True

        curNode = self.head
        while curNode is not None:
            # If none is reached, then pile does not contain given title
            if curNode.next is None:
                return False
            # If next node is given title, remove next node
            elif curNode.next.title == title:
                curNode.next = curNode.next.next
                self.size -= 1
                return True
            curNode = curNode.next

    def removePosition(self, number):
        """
            removePosition() removes the book at the given position.

            Parameters:
                number (int): position of item to remove

            Return:
                bool: True if successful, else False
        """
        # Check for valid position
        if number < 1 or number > self.size:
            return False

        # Use indexing to return book title at given position
        # Use removeBook() on returned book title
        if self.removeBook(self[number]):
            return True
        return False

    def rename(self, oldTitle, newTitle):
        """
            rename() takes a given name and changes it to a new given name.
        Old name is removed and new name is added to preserve correct order.

            Parameters:
                oldTitle (string): Name to be removed
                newTitle (string): Name to be added

            Returns:
                bool: True if successful, else False
        """
        # Check if pile contains old title
        if not self.contains(oldTitle):
            return False
        # Check if pile does not contain new title
        if self.contains(newTitle):
            return False

        # Return True if successfully remove old book and added new book
        if self.removeBook(oldTitle) and self.addBook(newTitle):
            return True