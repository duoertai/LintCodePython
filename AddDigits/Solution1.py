class Solution1:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        while num >= 10:
            sum = 0
            while num > 0:
                sum += num % 10
                num /= 10

            num = sum
        return num
