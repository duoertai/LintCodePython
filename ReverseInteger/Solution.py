class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here

        n_abs = n
        if n < 0:
            n_abs = -n

        res = 0
        while n_abs > 0:
            res = res * 10 + n_abs % 10;
            n_abs /= 10

        if n < 0:
            res = -res

        if res > (1 << 31) - 1 or res < -(1 << 31) - 1:
            return 0

        return res
