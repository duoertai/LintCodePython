class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        if n <= 0:
            return ""

        if n == 1:
            return "1"

        curr = "1"
        next = ""

        for i in range(1, n):
            p = 1
            num = 1
            c = curr[0]

            while p <= len(curr):
                while p < len(curr) and curr[p] == c:
                    p += 1
                    num += 1

                next = next + str(num) + str(c)

                if p == len(curr):
                    break

                c = curr[p]
                p += 1
                num = 1

            curr = next
            next = ""

        return curr
