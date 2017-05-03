class Solution2:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        # Write your code here
        if num < 10:
            return num

        if num % 9 == 0:
            return 9
        else:
            return num % 9
