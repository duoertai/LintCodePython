class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        if m == 1 or n == 1:
            return 1

        count = []
        for i in range(0, m):
            count.append([1])
        for i in range(0, n - 1):
            count[0].append(1)

        for i in range(1, m):
            for j in range(1, n):
                count[i].append(count[i - 1][j] + count[i][-1])

        return count[m - 1][n - 1]
