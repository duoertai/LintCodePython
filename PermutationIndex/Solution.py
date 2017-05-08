class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        if A is None or len(A) <= 1:
            return 1

        res = 1

        for i in range(0, len(A)):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1

            res += smaller * self.factor(len(A) - i - 1)

        return res

    def factor(self, n):
        if n <= 1:
            return 1

        res = 1
        for i in range(1, n + 1):
            res *= i

        return res
