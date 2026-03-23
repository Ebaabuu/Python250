from arrays import Array
from math import ceil

# @author Emaad Gafoor
class Deck:
    """
        Deck represents a deck of cards. It holds an array of strings,
    each of which represents a card. Deck objects can be reorganized
    or return a portion of the array.

        Member Variables:
            _items(array): Holds the array of "card" strings sent in
            by the user.
    """
    def __init__(self, array):
        """
            Constructs Deck class with entered array.

            Parameters:
                array(array): Array object which represents a group
                of cards.
        """
        self.__items = array

    def __str__(self):
        """
            Returns Deck as a formatted string.

            Returns:
                string: Lists each card in the deck with
                spaces separating them
        """
        deckAsString = ""
        for card in self.__items:
            deckAsString += card + " "
        deckAsString = deckAsString.rstrip()
        return deckAsString

    def size(self):
        """
            Returns number of elements in the __items member variable
        for Deck objects

            Returns:
                int: Number of elements in array
        """
        return len(self.__items)

    def load(self, array):
        """
            Loads a Deck of cards with the given array

            Parameters:
                array(array): Array object which represents a group
                of cards.
        """
        self.__items = array

    def cutTop(self):
        """
            Returns the first half of the Deck. If there is an odd number
        of cards, returns the lesser half of the deck.

            Returns:
                string: array of first half of cards
        """
        topHalf = Array(self.size() // 2)
        for i in range(len(topHalf)):
            topHalf[i] = self.__items[i]
        return topHalf

    def cutBottom(self):
        """
            Returns the second half of the Deck. If there is an odd number
        of cards, returns the greater half of the deck.

            Returns:
                string: array of second half of cards
         """
        bottomHalf = Array(ceil(self.size() / 2)) # Round up size of Array

        originalIndex = self.size() - 1 # track index value of the original array
        for i in range(len(bottomHalf) - 1, -1, -1):
            bottomHalf[i] = self.__items[originalIndex]
            originalIndex -= 1

        return bottomHalf

    def rotate(self):
        """
            Swaps the first and second half of the Deck and
        assigns the new array to the __items member variable.
        """
        rotatedDeck = Array(len(self.__items))

        topHalf = self.cutTop()
        bottomHalf = self.cutBottom()

        for i in range(len(bottomHalf)):
            rotatedDeck[i] = bottomHalf[i]

        topHalfIndex = 0 # Track index of array with top half
        for i in range(len(bottomHalf), len(rotatedDeck)):
            rotatedDeck[i] = topHalf[topHalfIndex]
            topHalfIndex += 1

        self.__items = rotatedDeck

    def reverse(self):
        """
            Reverses the order of the Deck and assigns the
        new array to the __items member variable.
        """
        reversedDeck = Array(len(self.__items))

        # Reverse index numbers to reverse Array order
        reversedIndex = len(self.__items) - 1
        for i in range(len(self.__items)):
            reversedDeck[i] = self.__items[reversedIndex]
            reversedIndex -= 1

        self.__items = reversedDeck

    def shuffle(self):
        """
            Performs a perfect out-shuffle which retains the top
        and bottom cards shuffles the rest of the cards by using
        an algorithm to sort them to swap between cards in the
        first half and the second half of the Deck. Updates the
        Deck's __items value with the new shuffled Deck.
        """
        if len(self.__items) <= 1:
            return 0

        shuffledDeck = Array(len(self.__items))
        topHalf = self.cutTop()
        bottomHalf = self.cutBottom()

        # Swap between odd and even index values to decide when to place
        # cards in either the top half Deck or bottom half Deck.
        isEven = True
        topHalfCounter = 0
        bottomHalfCounter = 0
        for i in range(len(shuffledDeck)):

            # Store value at final index in the case of odd numbers
            if i == len(shuffledDeck) - 1:
                shuffledDeck[i] = bottomHalf[len(bottomHalf) - 1]
            elif isEven:
                shuffledDeck[i] = topHalf[topHalfCounter]
                topHalfCounter += 1
            else:
                shuffledDeck[i] = bottomHalf[bottomHalfCounter]
                bottomHalfCounter += 1
            isEven = not isEven # Swap between even and odd after every loop

        self.__items = shuffledDeck