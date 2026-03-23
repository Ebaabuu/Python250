from sorts import *
from arrays import Array

def main():
    print("***Testing Selection Sort***")
    
    a = Array(7)
    a[0] = "C"
    a[1] = "E"
    a[2] = "F"
    a[3] = "A"
    a[4] = "G"
    a[5] = "Z"
    a[6] = "D"
    selectionSort(a)
    print(a)
    
    b = Array(7)
    b[0] = 9
    b[1] = 5
    b[2] = 1
    b[3] = 400
    b[4] = -1
    b[5] = 12
    b[6] = 84
    selectionSort(b)
    print(b)
    
    print("\n***Testing Bubble Sort***")
    
    a = Array(7)
    a[0] = "C"
    a[1] = "E"
    a[2] = "F"
    a[3] = "A"
    a[4] = "G"
    a[5] = "Z"
    a[6] = "D"
    bubbleSort(a)
    print(a)
    
    b = Array(7)
    b[0] = 9
    b[1] = 5
    b[2] = 1
    b[3] = 400
    b[4] = -1
    b[5] = 12
    b[6] = 84
    bubbleSort(b)
    print(b) 
    
    print("\n***Testing Insertion Sort (descending)***")
    
    a = Array(7)
    a[0] = "C"
    a[1] = "E"
    a[2] = "F"
    a[3] = "A"
    a[4] = "G"
    a[5] = "Z"
    a[6] = "D"
    insertionSort(a, "descending")
    print(a)
    
    b = Array(7)
    b[0] = 9
    b[1] = 5
    b[2] = 1
    b[3] = 400
    b[4] = -1
    b[5] = 12
    b[6] = 84
    insertionSort(b, "descending")
    print(b)

    print("\n***Testing Insertion Sort (ascending)***")

    a = Array(7)
    a[0] = "C"
    a[1] = "E"
    a[2] = "F"
    a[3] = "A"
    a[4] = "G"
    a[5] = "Z"
    a[6] = "D"
    insertionSort(a, "ascending")
    print(a)

    b = Array(7)
    b[0] = 9
    b[1] = 5
    b[2] = 1
    b[3] = 400
    b[4] = -1
    b[5] = 12
    b[6] = 84
    insertionSort(b, "ascending")
    print(b)

    print("\n***Testing Insertion Sort (invalid)***")
    
    a = Array(7)
    a[0] = "C"
    a[1] = "E"
    a[2] = "F"
    a[3] = "A"
    a[4] = "G"
    a[5] = "Z"
    a[6] = "D"
    insertionSort(a, "up")
    print(a)
    
    b = Array(7)
    b[0] = 9
    b[1] = 5
    b[2] = 1
    b[3] = 400
    b[4] = -1
    b[5] = 12
    b[6] = 84
    insertionSort(b, "down")
    print(b)     

if __name__ == "__main__":
    main()