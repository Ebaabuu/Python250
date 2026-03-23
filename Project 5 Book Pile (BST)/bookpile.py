"""
@author Emaad Gafoor
file: bookpile.py
"""
from book import Book
class BookPile:
    """
        Bookpile object represents a pile of books ordered into a
    Binary Search Tree based on title length, with longer names placed
    first. If two or more Books share the same title length, they are
    placed in alphabetical order.

        Member Variables:
            root(book): Reference to root node in BST
            size(int): Number of books in tree
    """

    def __init__(self,  books = None):
        # initialize empty BookPile with clear().
        self.clear()

        # Add items from given source.
        if books is not None:
            for book in books:
                self.addBook(book)

    def __len__(self):
        return self.size

    def __eq__(self, other):

        # Check if objects are the same.
        if self is other:
            return True

        # Check if their types are different.
        if type(self) != type(other):
            return False

        # Check if their size differs.
        if len(self) != len(other):
            return False

        # iterate through each item and check if
        # they are equal.
        for item in self:
            if item not in other:
                return False

        return True

    def clear(self):
        """
           clear() initializes an empty BookPile.
        """
        self.root = None
        self.size = 0

    def isEmpty(self):
        """
           isEmpty() returns true if BookPile is Empty.

           Returns:
               bool: True if BookPile is empty, else False
        """
        return True if self.size == 0 else False

    def addBook(self, title):
        """
            addBook() adds a given book from given title into the
        bookpile BST. The new book must have a title with at least
        one character and no repeated titles.

            Parameters:
                title (string): Name of book being inserted

            Returns:
                bool: True if book is added, else False
        """

        # Check if title has at least one character.
        if title == "":
            return False

        # Tree is empty, place new item at the root.
        if self.isEmpty():
            self.root = Book(title)

        # BookPile already contains item, do not add.
        elif self.contains(title):
            return False

        # Search for the item's spot and add title.
        else:
            self.__addHelper(self.root, title)

        self.size += 1
        return True

    def __addHelper(self, subTreeRef, title):
        """
            __addHelper() is given a subtree to search and a title to insert.
        If title is not found in the given subtree's title, __addHelper() is
        recursively called on the left or right child given the title's
        length: left child is length is greater, right child if length is
        lesser. If both lengths are equal, then left child if title precedes
        subtree's title alphabetically, else right child.

            Parameters:
                subTreeRef (Book): Book to be compared to title
                title (string): Name of book being inserted
        """
        # For a given title, search for proper spot in BookPile
        # and link book there.

        # Search left child if title length is greater than current observed title.
        if len(title) > len(subTreeRef.title):
            # Place in left child if empty, else call __addhelper()
            # on left child.
            if subTreeRef.leftChildRef is None:
                subTreeRef.leftChildRef = Book(title)
            else:
                self.__addHelper(subTreeRef.leftChildRef, title)

        # if titles have equal length:
        elif len(title) == len(subTreeRef.title):
            # Place the new title to the right of observed title if it
            # exceeds the observed title in alphabetical order, else
            # place in right child.
            if title > subTreeRef.title:
                # Place in right child if empty, else call __addhelper()
                # on right child.
                if subTreeRef.rightChildRef is None:
                    subTreeRef.rightChildRef = Book(title)
                else:
                    self.__addHelper(subTreeRef.rightChildRef, title)

            else:
                # Place in left child if empty, else call __addhelper()
                # on left child.
                if subTreeRef.leftChildRef is None:
                    subTreeRef.leftChildRef = Book(title)
                else:
                    self.__addHelper(subTreeRef.leftChildRef, title)

        # New title must have a smaller length, place in right child or
        # call __addhelper() if right child is occupied.
        else:
            if subTreeRef.rightChildRef is None:
                subTreeRef.rightChildRef = Book(title)
            else:
                self.__addHelper(subTreeRef.rightChildRef, title)

    def __iter__(self):
        # Return an iterable list of an inorder traversal of the BookPile.
        return iter(self.inorder())

    def inorder(self):
        """
            inorder() returns a list of every item in the BookPile in
        order by length from longest to shortest. If two or more titles
        share the same length, then alphabetical order is used.

            Returns:
                list: True if book is added, else False
        """
        # Return a list of titles in BookPile in order.

        lyst = list()
        self.__inorderHelper(self.root, lyst)
        return lyst

    def __inorderHelper(self, book, lyst):
        """
            __inorderHelper traverses the BookPile with an inorder traversal
        through recursive calls to left child, then calls to right children.

            Parameters:
                book (Book): current book to either be appended or traversed
                lyst (list): titles appended to lyst
        """

        if book is not None:
            self.__inorderHelper(book.leftChildRef, lyst)
            lyst.append(book.title)
            self.__inorderHelper(book.rightChildRef, lyst)

    def contains(self, title):
        """
            contains() returns the outcome of __findHelper(), which determines
        whether title is found in the BookPile.

            Parameters:
                title (string): title to be found in BookPile

            Returns:
                bool: True if found, else False
        """
        return self.__findHelper(self.root, title)

    def __findHelper(self, subTreeRef, title):
        """
            __findHelper() does a binary search through BookPile to find
        given title.

            Parameters:
                subTreeRef (Book): Node to be compared to title
                title (string): Name of book being searched for

            Returns:
                bool: True if found, else False
        """

        # Given title not found, return False.
        if subTreeRef is None:
            return False

        # Given title found, return True.
        elif subTreeRef.title == title:
            return True

        # If given title length is greater than observed title, search
        # right child.
        elif len(title) > len(subTreeRef.title):
            return self.__findHelper(subTreeRef.leftChildRef, title)

        # If title lengths are equal, search right child if given title
        # precedes observed title alphabetically, else search left child.
        elif len(title) == len(subTreeRef.title):
            if title > subTreeRef.title:
                return self.__findHelper(subTreeRef.rightChildRef, title)
            else:
                return self.__findHelper(subTreeRef.leftChildRef, title)
        # Search right child
        else:
            return self.__findHelper(subTreeRef.rightChildRef, title)

    def __str__(self):
        if self.isEmpty():
            return "Book pile is empty."

        # Create list with items in order and iterate with each item
        # appended onto bookString. Return bookString.
        bookList = self.inorder()
        bookString = ""
        for i in range(len(bookList)):
            bookString += f"{i + 1}. {bookList[i]} ({len(bookList[i])})\n"

        return bookString

    def bookPosition(self, title):
        """
            bookPosition() returns the position of a given title in the
        BookPile in order by length starting at index 1.

            Parameters:
                title (string): Name of book being observed

            Returns:
                int: index of book being observed, -1 if not found
        """
        if not self.contains(title):
            return -1

        # Create list with items in order and return proper index.
        bookList = self.inorder()
        return bookList.index(title) + 1

    def __getitem__(self, position):
        # Validate position with index starting at 1
        if not 0 < position <= self.size:
            raise IndexError("ERROR: Invalid position.")

        return self.inorder()[position - 1]

    def removeBook(self, title):
        """
            removeBook() removes a book with the given title and returns
        true if successful.

            Parameters:
                title (string): Name of book being removed

            Returns:
                bool: True if book is removed, else False
        """

        if not self.contains(title):
            return False

        # Set root to BookPile with title removed with
        # __locateBookAndRemove().
        self.root = self.__locateBookToRemove(self.root, title)
        self.size -= 1
        return True

    def __locateBookToRemove(self, subTreeBook, title):
        """
           __locateBookAndRemove() locates the book to be removed with
        the given title and calls __removeBook() to properly remove it.

           Parameters:
               title (string): Name of book being located
               subTreeBook (Book): Name of book observed

           Returns:
               Book: subtree of Book if book is found, else None
        """

        # If we don't find the target in the tree
        if subTreeBook is None:
            return None

        # Found the target in the root of this subtree
        if subTreeBook.title == title:
            return self.__removeBook(subTreeBook)

        if len(title) < len(subTreeBook.title):
            # If given title length is smaller, recursive call to
            # right child.
            subTreeBook.rightChildRef = \
                (self.__locateBookToRemove
                (subTreeBook.rightChildRef, title))
        elif len(title) == len(subTreeBook.title):
            # If they share the same length, recursive call to left
            # child if given title alphabetically precedes observed
            # title, else recursive call to right child.
            if title < subTreeBook.title:
                subTreeBook.leftChildRef = \
                    (self.__locateBookToRemove
                    (subTreeBook.leftChildRef, title))
            else:
                subTreeBook.rightChildRef = \
                    (self.__locateBookToRemove
                    (subTreeBook.rightChildRef, title))
        else:
            # Recursive call to left child.
            subTreeBook.leftChildRef = \
                (self.__locateBookToRemove
                (subTreeBook.leftChildRef, title))
        return subTreeBook

    def __removeBook(self, book):
        """
           __removeBook() removes a book from a BookPile.

           Parameters:
               book (Book): Book to be removed.

           Returns:
               Book: BookPile with book removed.
        """

        # Check if node is a leaf.
        if book.leftChildRef is None and book.rightChildRef is None:
            return None

        # Check if node has only one child.
        if book.leftChildRef is None:
            return book.rightChildRef
        elif book.rightChildRef is None:
            return book.leftChildRef

        # Node has two children. Replace the item in the
        # node with its in order successor.
        iosBook = book.rightChildRef
        while iosBook.leftChildRef is not None:
            iosBook = iosBook.leftChildRef

        # Backup the data in the node being swapped so it's not lost.
        iosBackup = iosBook.title
        # Call removeBook() on swapped node which contains title
        # to be removed.
        self.removeBook(iosBook.title)
        # Increment size since removeBook was called again.
        self.size += 1
        book.title = iosBackup

        return book

    def removePosition(self, index):
        """
           removePosition() removes a book from a BookPile at the
        given index value.

           Parameters:
               index (int): index of Book to be removed

           Returns:
               Book: BookPile with book removed
        """
        if not 0 < index <= self.size:
            return False
        return self.removeBook(self.inorder()[index - 1])

    def rename(self, oldTitle, newTitle):
        """
           rename() renames a book and places it in its proper place.
        The Book with the old name is removed and a new Book with the
        given new name is added.

           Parameters:
               oldTitle (string): Book to be removed
               newTitle (string): Book to be added

           Returns:
               bool: True if successful, else False
        """
        if newTitle == "":
            return False

        # Check if pile contains old title
        if not self.contains(oldTitle):
            return False
        # Check if pile does not contain new title
        if self.contains(newTitle):
            return False

        if self.removeBook(oldTitle) and self.addBook(newTitle):
            return True
        return False
