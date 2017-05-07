class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return 0

        if len(A) == 1:
            return 1

        res = 1

        l2r = []
        l2r.append(1)

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                l2r.append(l2r[i - 1] + 1)
                if l2r[-1] > res:
                    res = l2r[-1]
            else:
                l2r.append(1)

        r2l = []
        for i in range(0, len(A)):
            r2l.append(1)

        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                r2l[i] = r2l[i + 1] + 1
                if r2l[i] > res:
                    res = r2l[i]
            else:
                r2l[i] = 1

        return res
