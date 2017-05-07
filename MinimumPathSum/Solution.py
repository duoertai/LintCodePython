class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        res = []
        for i in range(0, m):
            res.append([])

        res[0].append(grid[0][0])

        for i in range(1, m):
            res[i].append(res[i - 1][0] + grid[i][0])
        for i in range(1, n):
            res[0].append(res[0][-1] + grid[0][i])

        for i in range(1, m):
            for j in range(1, n):
                res[i].append(min(res[i][-1], res[i - 1][j]) + grid[i][j])

        return res[m - 1][n - 1]
