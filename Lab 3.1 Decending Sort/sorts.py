from arrays import Array

#### SELECTION SORT ####

def findIndexOfSmallest(array, start):

    indexSoFar = start

    for currentIndex in range(start+1, len(array)):

        if array[currentIndex] > array[indexSoFar]:
            indexSoFar = currentIndex

    return indexSoFar

def selectionSort(array):

    for front in range(len(array) - 1):

        smallest = findIndexOfSmallest(array, front)
        array[front], array[smallest] = array[smallest], array[front]

#### BUBBLE SORT ####

def bubbleSort(array):
    sorted = False
    passNum = 1

    while not sorted and (passNum < len(array)):
        sorted = True

        for i in range(0, len(array) - passNum):
            next = i + 1

            if array[i] < array[next]:
                array[i], array[next] = array[next], array[i]
                sorted = False

        passNum += 1
        
#### INSERTION SORT ####
def insertionSort(array, order):
    if order == "ascending":
        for unsorted in range(1, len(array)):
            nextItem = array[unsorted]
            loc = unsorted

            while loc > 0 and array[loc - 1] > nextItem:
                array[loc] = array[loc - 1]
                loc -= 1

            array[loc] = nextItem
    elif order == "descending":
        for unsorted in range(1, len(array)):
            nextItem = array[unsorted]
            loc = unsorted

            while loc > 0 and array[loc - 1] < nextItem:
                array[loc] = array[loc - 1]
                loc -= 1

            array[loc] = nextItem