class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n <= 1:
            return 1

        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 2

        for i in range(0, n - 2):
            temp = a + b
            a = b
            b = temp

        return b
