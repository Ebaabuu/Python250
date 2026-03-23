from arraystack import ArrayStack
from arrays import Array

class SuperArrayStack(ArrayStack):

    def __getitem__(self, index):
        if index >= len(self) or index < 0:
            raise KeyError("ERROR: Invalid index accessed.")

        return self.items[len(self) - index - 1]

    def __setitem__(self, index, item):
        if index >= len(self) or index < 0:
            raise KeyError("ERROR: Invalid index accessed.")

        self.items[len(self) - index - 1] = item

    def insert(self, index, newItem):

        if index >= len(self) + 1:
            raise KeyError("ERROR: Invalid index accessed.")

        index = len(self) - index # Flips to the proper index

        if self.size == len(self.items):
            temp = Array(2 * len(self))

            for i in range(len(self)):
                temp[i] = self.items[i]

            self.items = temp

        for i in range(len(self), index - 1, -1):
            self.items[i] = self.items[i - 1]

        self.items[index] = newItem

        self.size += 1

    def remove(self, item):
        indexFound = -1

        for i in range(len(self)):
            if self[i] == item:
                indexFound = i
                break

        if indexFound < 0:
            return False

        for i in range(indexFound, 0, -1):
            self[i] = self[i - 1]

        self.size -= 1

        # Check array memory here and decrease it if necessary
        if self.size <= (len(self.items) // 4):

            # Don't allow size to go below DEFAULT_CAPACITY
            if ArrayStack.DEFAULT_CAPACITY > len(self.items) // 2:
                newSize = ArrayStack.DEFAULT_CAPACITY
            else:
                newSize = len(self.items) // 2

            temp = Array(newSize)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp

        return True

    def sort(self):
        pass