class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None or len(obstacleGrid) == 0 or obstacleGrid[0] is None or len(obstacleGrid[0]) == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        count = []
        i = 0

        while i < m:
            if obstacleGrid[i][0] == 0:
                count.append([1])
                i += 1
            else:
                while i < m:
                    count.append([0])
                    i += 1

        i = 1
        while i < n:
            if obstacleGrid[0][i] == 0:
                count[0].append(1)
                i += 1
            else:
                while i < n:
                    count[0].append(0)
                    i += 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    count[i].append(count[i - 1][j] + count[i][-1])
                else:
                    count[i].append(0)

        return count[m - 1][n - 1]
