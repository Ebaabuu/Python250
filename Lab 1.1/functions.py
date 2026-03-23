from arrays import Array


def populateArray(myArray, start, increment):
    for i in range(len(myArray)):
        myArray[i] = start + (i * increment)


def reverseArray(myArray):
    newArray = Array(len(myArray))
    for i in range(len(myArray)):
        newArray[i] = myArray[len(myArray) - (i + 1)]

    return newArray


def combineArrays(firstArray, secondArray):
    combinedArray = Array(len(firstArray) + len(secondArray))

    for i in range(len(firstArray)):
        combinedArray[i] = firstArray[i]

    for i in range(len(secondArray)):
        combinedArray[i + len(firstArray)] = secondArray[i]

    return combinedArray
