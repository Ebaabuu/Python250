def displayCol(lyst, col):
    """Displays the indicated column from a 2D list on the screen. """

    # Step 1
    for row in lyst:
        if len(row) > col:
            print(row[col])
def avg(lyst):
    """Returns the mean of a 2D list of numbers."""

    # Step 2
    total = 0
    numElements = 0
    for row in lyst:
        for col in row:
            total += col
            numElements += 1
    return total / numElements


def sum(lyst):
    """Returns the sum of a 2D list of numbers."""

    # Step 3
    total = 0
    for row in lyst:
        for col in row:
            total += col
    return total
    
def smallest(lyst):
    """Returns the smallest number in of a 2D list of numbers."""
    
    # Step 4
    small = lyst[0][0]
    for row in lyst:
        for col in row:
            if col < small:
                small = col

    return small

def main():
    """Tests the functions."""
    
    lyst = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

    print("Column 1:")
    displayCol(lyst, 0)
    print()

    print(f"Sum: {sum(lyst):.2f}")
    print(f"Smallest: {smallest(lyst):.2f}")
    print(f"Average: {avg(lyst):.2f}")

# The entry point for program execution
if __name__ == "__main__":
    main()
     
    
        
