class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or matrix[0] is None or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left < right:
            mid = left + (right - left) / 2
            row = mid / n
            col = mid % n

            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return matrix[left / n][left % n] == target
