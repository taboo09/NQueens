class Board(object):

    def __init__(self, size):
        self.size = size
        self.board = [['-' for i in range(self.size)] for i in range(self.size)]

    def print_board(self):
        print("  ", end="")
        for i in range(self.size):
            print(i,end="  ")
        print()

        for i in range(self.size):
            print(i,end=" ")

            for j in range(self.size):
                print(self.board[i][j], end = "  ")
            print()

    #place a queen on the board 
    def place_queen(self, row, column):
        self.board[row][column] = 'Q'
        return board

    #remove a queen from the board
    def remove_queen(self, row, column):
        self.board[row][column] = '-'
        return board
    
    
    #checking for an available position
    def check_queen(self, row, column):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'Q':
                    if ((i == row) or
                        (j == column) or
                        (i - j == row - column) or
                        (i + j == row + column)):
                        return False
        return True
                            
    #return a solution of N queens on NxN board
    def nQueens(self, column = 0):
        #base case
        if column >= self.size:
            self.print_board()
            return True
        else:
            for rows in range(self.size):
                if self.check_queen(rows, column):   
                    #place a queen on the board
                    self.place_queen(rows, column)

                    #take another step using recursion
                    solution = self.nQueens(column + 1)

                    if solution:
                        return True

                    #remove a queen from the board
                    self.remove_queen(rows, column)

            return False
    


board = Board(8)

board.nQueens()


#solution is:

#      0  1  2  3  4  5  6  7
#    0 Q  -  -  -  -  -  -  -
#    1 -  -  -  -  -  -  Q  -
#    2 -  -  -  -  Q  -  -  -
#    3 -  -  -  -  -  -  -  Q
#    4 -  Q  -  -  -  -  -  -
#    5 -  -  -  Q  -  -  -  -
#    6 -  -  -  -  -  Q  -  -
#    7 -  -  Q  -  -  -  -  -

