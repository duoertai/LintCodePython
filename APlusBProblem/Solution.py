class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        res = 0
        c = 0

        for i in range(0, 32):
            res = res | (((a >> i) & 1) ^ ((b >> i) & 1) ^ c) << i
            c = (((a >> i) & 1) ^ ((b >> i) & 1)) & c | (((a >> i) & 1) & ((b >> i) & 1))
        return res
