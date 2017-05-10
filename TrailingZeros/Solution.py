class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        i = 5
        res = 0

        while i <= n:
            res += n / i
            i *= 5

        return res
