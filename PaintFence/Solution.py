class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        # Write your code here
        if n == 1:
            return k
        if n == 2:
            return k * k

        if k == 1 and n > 2:
            return 0

        same = []
        diff = []
        for i in range(0, n):
            same.append(0)
            diff.append(0)

        same[0] = k
        same[1] = k
        diff[0] = k
        diff[1] = k * (k - 1)

        for i in range(2, n):
            same[i] = diff[i - 1]
            diff[i] = same[i - 1] * (k - 1) + diff[i - 1] * (k - 1)

        return same[n - 1] + diff[n - 1]
