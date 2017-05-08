class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j]:
                    res += 1
                    self.flip(grid, i, j)

        return res

    def flip(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or i >= m or j < 0 or j >= n:
            return

        if grid[i][j]:
            grid[i][j] = False
            self.flip(grid, i - 1, j)
            self.flip(grid, i + 1, j)
            self.flip(grid, i, j - 1)
            self.flip(grid, i, j + 1)

        return
