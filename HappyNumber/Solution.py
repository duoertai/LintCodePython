class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        if n <= 0:
            return False

        if n == 1:
            return True

        s = set()

        while True:
            if n in s:
                return False

            s.add(n)
            next = 0

            while n > 0:
                next += (n % 10) * (n % 10)
                n /= 10

            if next == 1:
                return True

            n = next

        return False
