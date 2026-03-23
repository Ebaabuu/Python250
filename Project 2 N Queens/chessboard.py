"""
@author Emaad Gafoor
file: chessboard.py
"""
class ChessBoard:
    """
    ChessBoard object describes a chessboard of varied
size. The ChessBoard will place N number of Queens on
the board depending on the given size.

    Member Variables:
        board (array): Multidimensional Array Representing Chess Board, default 8
        boardSize(int): Size of Board and Number of Queens
    """
    def __init__(self, boardSize = 8):

        self.board = []
        self.boardSize = boardSize
        self.setSize(self.boardSize)

    def setSize(self, boardSize = 0):
        """
        setSize() resets the board with the given board size, with
    default size being 8. Size is readjusted if the board size is
    smaller than 4 or greater than 12.

        Parameters:
            boardSize (int): Size of board
        """
        self.board = []
        if boardSize < 4:
            self.boardSize = 4
        elif boardSize > 12:
            self.boardSize = 12
        else:
            self.boardSize = boardSize

        for i in range(self.boardSize):
            tmpBoard = []
            for i in range(self.boardSize):
                tmpBoard.append("*")
            self.board.append(tmpBoard)

    def getSize(self):
        """
        getSize returns the size of one end of the board.

        Returns:
            int: Size of one end of the board.
        """
        return self.boardSize

    def displayBoard(self):
        """
        displayBoard prints the board by displaying each row one by one and
    ending with a newline.
        """
        for row in self.board:
            for col in row:
                print(col, end = " ")
            print()

    def solve(self):
        """
        solve places a Queen in each column by calling placeQueens.
    If placeQueens ever fails and returns False, solve will return
    False. If N Queens are successfully placed, returns True.
        Returns:
            bool: False if placeQueens returns False, True if
        placeQueens returns True.
        """
        for i in range(self.boardSize): # iterate through each column of Chessboard
            if not self.placeQueens(i):
                return False
            return True

    def safeSpace(self, row, column):
        """
        safeSpace observes the spaces to the left, upper left, and lower left of
    the current space chosen to determine if any other Queens may attack the
    current space.

        Parameters:
            row (int): The vertical position of the observed space.
            column (int): The horizontal position of the observed space.

        Returns:
            bool: True if the space isn't targeted, False if the space
        is being targeted.
        """
        isSafe = True
        # Check left side of piece
        for i in range(column):
            if self.board[row][i] == "Q":
                isSafe = False

        # Check bottom left pieces
        i = row
        j = column
        while ((i >= 0 and j >= 0) and
               (i <= self.boardSize - 1 and j <= self.boardSize - 1)):
            if self.board[i][j] == "Q":
                isSafe = False
            i += 1
            j -= 1

        # Check top left pieces
        i = row
        j = column
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                isSafe = False
            i -= 1
            j -= 1

        return isSafe

    def placeQueens(self, column):
        """
        placeQueens goes through the column starting at row 0 and places
    a Queen at the first safe row, iterating through any unsafe ones. It
    then recursively checks the next row to see if placing a piece is possible.
    It will continue to check and place pieces until the final column is reached
    and all Queens are placed. If a space is found to be unsafe, it will recursively
    return to the last safe space and try a different space until the next space can
    be placed safely.

        Parameters:
            column (int): The observed column of which a Queen will be placed in.

        Returns:
            bool: True if the column has had a Queen placed, False if impossible to
        place a Queen.
        """
        row = 0
        # Once the final column as been reached and placed, the board is solved.
        if column >= self.boardSize:
            return True
        else:
            while row < self.boardSize:
                # Check if safe and place Queen
                if self.safeSpace(row, column):
                    self.board[row][column] = "Q"

                    # Try to place a Queen in the next column. If unsafe, place '*' and
                    # return to the previous recursive instance.
                    if not self.placeQueens(column + 1):
                        self.board[row][column] = "*"
                        row += 1
                    else:
                        return True
                else:
                    row += 1
            return False