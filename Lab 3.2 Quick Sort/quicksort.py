from arrays import Array

def insertionSort(array):

    for unsorted in range(1, len(array)):
        nextItem = array[unsorted]
        loc = unsorted

        while loc > 0 and array[loc - 1] > nextItem:
            array[loc] = array[loc - 1]
            loc -= 1

        array[loc] = nextItem

def quickSort(theArray, first, last):

    if (last - first + 1) <= 3:
        insertionSort(theArray)
    
    else:
        pivot_index = partition(theArray, first, last)
    
        quickSort(theArray, first, pivot_index - 1)
        quickSort(theArray, pivot_index + 1, last)

def partition(theArray, first, last):

    # Caculate the middle of the range.
    mid = (first + last) // 2
    
    # STEP 1
    newArray = Array(3)
    newArray[0] = theArray[first]
    newArray[1] = theArray[mid]
    newArray[2] = theArray[last]
    insertionSort(newArray)
    theArray[first] = newArray[0]
    theArray[mid] = newArray[1]
    theArray[last] = newArray[2]
    
    # STEP 2
    temp = theArray[mid]
    theArray[mid] = theArray[last - 1]
    theArray[last - 1] = temp

    pivotIndex = last - 1
    pivot = theArray[pivotIndex]

    indexFromLeft = first + 1
    indexFromRight = last - 2

    done = False
    while not done:

        # STEP 3
        while theArray[indexFromLeft] < pivot:
            indexFromLeft += 1
            
        # STEP 4
        while theArray[indexFromRight] > pivot:
            indexFromRight -= 1
            
        # STEP 5
        if indexFromLeft < indexFromRight:
            temp = theArray[indexFromLeft]
            theArray[indexFromLeft] = theArray[indexFromRight]
            theArray[indexFromRight] = temp
            indexFromLeft += 1
            indexFromRight -= 1

        else:
            done = True
    
    # STEP 6
    temp = theArray[pivotIndex]
    theArray[pivotIndex] = theArray[indexFromLeft]
    theArray[indexFromLeft] = temp
    pivotIndex = indexFromLeft
    
    return pivotIndex


