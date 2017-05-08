class Solution:
    """
    @param n: An integer
    @return: True or false
    """

    def checkPowerOf2(self, n):
        # write your code here
        if n <= 0:
            return False

        count = 0

        for i in range(0, 32):
            if ((n >> i) & 1) == 1:
                count += 1
                if count > 1:
                    return False

        return count == 1
