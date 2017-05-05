class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        diff = a ^ b
        count = 0
        for i in range(0, 32):
            if ((diff >> i) & 1) == 1:
                count += 1

        return count
