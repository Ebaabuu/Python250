from chessboard import ChessBoard


def main():
    # Create a board
    myBoard = ChessBoard()
    sixBoard = ChessBoard(0)

    # Display the default board:
    print("The default unsolved board:")
    myBoard.displayBoard()
    print()

    print("Default Solved Board:")
    if myBoard.solve():
        print("True")
        myBoard.displayBoard()

    print()
    sixBoard.setSize(6)

    print("Size 6 Solved Board")
    if sixBoard.solve():
        print("true")
        sixBoard.displayBoard()
    else:
        print("false")
        sixBoard.displayBoard()

    print()

    print("Loop Through Boards")
    # Loop through board sizes from 3 to 13.
    # Since 3 and 13 are invalid you should see
    # board sizes 4 and 12 twice.
    for i in range(3, 14):
        myBoard.setSize(i)

        # Attempt to solve the N-Queens Problem. If the solve
        # code is working it should find solutions for all
        # sizes from 4 through 12.
        if not myBoard.solve():
            print(f"Sorry, no solution was found for board size {myBoard.getSize()}.")
            print("The final board is:")
            myBoard.displayBoard()
            print()
        else:
            print(f"Size {myBoard.getSize()} solution:")
            myBoard.displayBoard()
            print()


if __name__ == "__main__":
    main()
