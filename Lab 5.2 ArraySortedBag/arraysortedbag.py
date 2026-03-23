from arraybag import ArrayBag
from arrays import Array
class ArraySortedBag(ArrayBag):
    """An array-based bag implementation."""
    def add(self, item):
        """Adds item to self."""

        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            temp = Array(2 * len(self))

            for i in range(len(self)):
                temp[i] = self.items[i]

            self.items = temp

        # Store the new item
        if self.size == 0:
            self.items[0] = item
        elif item >= self.items[self.size - 1]:
            self.items[self.size] = item
        else:
            addIndex = 0
            for i in range(self.size):
                if item >= self.items[i]:
                    addIndex += 1

            for i in range(self.size, addIndex, -1):
                self.items[i] = self.items[i - 1]
            self.items[addIndex] = item

        self.size += 1


    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""

        # Check array memory here and increase it if necessary
        if self.size == len(self.items):
            temp = Array(2 * len(self))

            for i in range(len(self)):
                temp[i] = self.items[i]

            self.items = temp

        itemIndex = self.getIndex(item)
        if itemIndex == -1:
            raise KeyError("ERROR: Item not found")

        for i in range(itemIndex, self.size):
            self.items[i] = self.items[i + 1]

        self.size -= 1

        # Check array memory here and decrease it if necessary
        if self.size <= (len(self.items) // 4):

            # Don't allow size to go below DEFAULT_CAPACITY
            if ArrayBag.DEFAULT_CAPACITY > len(self.items) // 2:
                newSize = ArrayBag.DEFAULT_CAPACITY
            else:
                newSize = len(self.items) // 2

            temp = Array(newSize)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp

    def getIndex(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                return i
        return -1