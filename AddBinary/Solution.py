class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        p1 = len(a) - 1
        p2 = len(b) - 1

        res = ""
        carry = 0

        while p1 >= 0 or p2 >= 0:
            bit1 = 0
            if p1 >= 0:
                bit1 = int(a[p1])
                p1 -= 1

            bit2 = 0
            if p2 >= 0:
                bit2 = int(b[p2])
                p2 -= 1

            res = str((bit1 + bit2 + carry) % 2) + res
            carry = (bit1 + bit2 + carry) / 2

        if carry == 1:
            res = "1" + res

        return res
