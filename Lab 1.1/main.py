from arrays import Array
from functions import *


def main():
    myArray = Array(5)

    print("Original default array:")
    print(myArray, " (Size:", len(myArray), ")", sep='')
    print()

    start = 7
    factor = 3

    populateArray(myArray, start, factor)

    print("Populated array:")
    print(myArray, " (Size:", len(myArray), ")", sep='')
    print()

    newArray = reverseArray(myArray)

    print("Original array (should be unchanged):")
    print(myArray, " (Size:", len(myArray), ")", sep='')
    print()

    print("Reversed array:")
    print(newArray, " (Size:", len(newArray), ")", sep='')
    print()

    otherArray = Array(7, 999)

    combined = combineArrays(myArray, otherArray)

    print("Original first array (should be unchanged):")
    print(myArray, " (Size:", len(myArray), ")", sep='')
    print()

    print("Original second array (should be unchanged):")
    print(otherArray, " (Size:", len(otherArray), ")", sep='')
    print()

    print("Combined array:")
    print(combined, " (Size:", len(combined), ")", sep='')
    print()


if __name__ == "__main__":
    main()
