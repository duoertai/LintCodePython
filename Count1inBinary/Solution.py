class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        for i in range(0, 32):
            if ((num >> i) & 1) == 1:
                count += 1

        return count
