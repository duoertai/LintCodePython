class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0 or matrix[0] is None or len(matrix[0]) == 0:
            return []

        res = []
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = 0
        upright = True

        for i in range(0, m * n):
            res.append(0)

        for i in range(0, m * n):
            res[i] = matrix[row][col]
            if upright:
                if row == 0 and col < n - 1:
                    col += 1
                    upright = not upright
                elif col == n - 1:
                    row += 1
                    upright = not upright
                else:
                    row -= 1
                    col += 1
            else:
                if col == 0 and row < m - 1:
                    row += 1
                    upright = not upright
                elif row == m - 1:
                    col += 1
                    upright = not upright
                else:
                    row += 1
                    col -= 1

        return res
