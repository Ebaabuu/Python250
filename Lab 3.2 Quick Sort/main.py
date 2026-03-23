from quicksort import quickSort
from quicksort import partition
from arrays import Array

def main():
    
    print("Partition test")
    a = Array(6)
    a[0] = 5
    a[1] = 2
    a[2] = 3
    a[3] = 1
    a[4] = 6
    a[5] = 4
    pivot = partition(a, 0, 5)
    print(f"pivot: {pivot}\npartitioned should be [3, 2, 1, 4, 6, 5]:\n{a}")
    
    print("Sorting 6 strings...")
    a = Array(6)
    a[0] = 5
    a[1] = 2
    a[2] = 6
    a[3] = 1
    a[4] = 3
    a[5] = 4

    quickSort(a, 0, 5)
    for i in range(6):
        print(a[i], end=" ")
    print("\n")
    
    print("Sorting 26 strings...")
    b = Array(26)
    
    # Populates the array with the alphabet backwards from Z to A using ASCII values
    for i in range(26):
        b[i] = chr(90 - i)

    quickSort(b, 0, 25)
    for i in range(26):
        print(b[i], end=" ")
    print("\n")
    
if __name__ == "__main__":
    main()