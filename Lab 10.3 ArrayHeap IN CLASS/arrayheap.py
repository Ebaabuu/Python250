"""
File: arrayheap.py

Defines the class ArrayHeap
"""

from heapinterface import HeapInterface
from arrays import Array


class ArrayHeap(HeapInterface):
    # Class variable
    DEFAULT_CAPACITY = 4  # small to force resizing

    def add(self, item):

        ################################
        # Double size if filled.
        if self.size == len(self.items):

            temp = Array(self.size * 2)

            for i in range(self.size):
                temp[i] = self.items[i]

            self.items = temp
            self.front = 0
            self.rear = self.size - 1
        # End of doubling size
        ################################

        self.items[self.size] = item
        newNodeIndex = self.size
        parentIndex = self.__getParentIndex(newNodeIndex)

        while newNodeIndex > 0 and self.items[newNodeIndex] >= self.items[parentIndex]:
            self.items[newNodeIndex], self.items[parentIndex] = (
                self.items[parentIndex], self.items[newNodeIndex])

            newNodeIndex = parentIndex
            parentIndex = self.__getParentIndex(newNodeIndex)

        self.size += 1

    def heapRebuild(self, subTreeRootIndex):

        if not self.__isLeaf(subTreeRootIndex):

            leftChildIndex = self.__getLeftChildIndex(subTreeRootIndex)
            rightChildIndex = self.__getRightChildIndex(subTreeRootIndex)
            largerChild = rightChildIndex

            if largerChild >= self.size or \
                    self.items[leftChildIndex] > self.items[largerChild]:
                largerChild = leftChildIndex

            if self.items[largerChild] > self.items[subTreeRootIndex]:
                self.items[largerChild], self.items[subTreeRootIndex] = (
                    self.items[subTreeRootIndex], self.items[largerChild])

                self.heapRebuild(largerChild)

    ################################
    # FUNCTIONS BELOW ARE COMPLETE #
    ################################

    def __isLeaf(self, nodeIndex):
        return (self.__getLeftChildIndex(nodeIndex) >= self.size)

    def peek(self):

        if self.isEmpty():
            raise AttributeError("Heap is empty")

        return self.items[0]

    def pop(self):

        if self.isEmpty():
            raise AttributeError("Heap is empty")

        poppedItem = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapRebuild(0)

        ###################################################################
        # Cut array size in half if we're using less than 1/4 of the array.
        # In the process, shift front to index 0.
        if self.size <= (len(self.items) // 4) \
                and (len(self.items) // 2) >= ArrayHeap.DEFAULT_CAPACITY:

            newSize = len(self.items) // 2

            temp = Array(newSize)
            for i in range(self.size):
                temp[i] = self.items[(self.front + i) % len(self.items)]
            self.items = temp
            self.front = 0
            self.rear = self.size - 1
        # End array resize
        ####################################################################

        return poppedItem

    def __getLeftChildIndex(self, nodeIndex):
        return (2 * nodeIndex) + 1

    def __getRightChildIndex(self, nodeIndex):
        return (2 * nodeIndex) + 2

    def __getParentIndex(self, nodeIndex):
        return (nodeIndex - 1) // 2

    def __iter__(self):

        # Strategy: copy items to a list, sort the list, return the iterator
        # for the list

        resultList = []
        for i in range(self.size):
            resultList.append(self.items[i])

        resultList.sort(reverse=True)  # sort descending

        return iter(resultList)

    def __str__(self):

        strHeap = ""

        # requires iterator
        for i in self:
            strHeap += str(i) + " "

        strHeap = "max -> " + strHeap + "<- min"

        return strHeap

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""

        return self.size == 0

    def __len__(self):
        """-Returns the number of items in self."""

        return self.size

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""

        newHeap = ArrayHeap(self)

        for i in other:
            newHeap.add(i)

        return newHeap

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""

        return str(self) == str(other)

    def clear(self):
        """Makes self become empty."""

        while not self.isEmpty(): self.pop()

    def __init__(self, sourceCollection=None):

        self.items = Array(ArrayHeap.DEFAULT_CAPACITY)
        self.size = 0

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
