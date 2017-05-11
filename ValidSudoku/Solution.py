class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(0, 9):
            row = set()
            col = set()
            sqr = set()

            for j in range(0, 9):
                if board[i][j] in row:
                    return False
                if board[i][j] != '.':
                    row.add(board[i][j])

                if board[j][i] in col:
                    return False
                if board[j][i] != '.':
                    col.add(board[j][i])

                if board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3] in sqr:
                    return False
                if board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3] != '.':
                    sqr.add(board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3])

        return True
