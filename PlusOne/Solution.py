class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        if digits is None or len(digits) == 0:
            return digits

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i]
            digits[i] = (temp + carry) % 10
            carry = (temp + carry) / 10

        if carry == 0:
            return digits
        else:
            digits.insert(0, 1)

        return digits
