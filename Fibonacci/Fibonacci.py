class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n <= 1:
            return 0
        if n == 2:
            return 1

        a = 0
        b = 1

        for i in range(n - 2):
            c = a + b
            a = b
            b = c

        return b