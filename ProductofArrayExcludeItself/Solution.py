class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return []

        left = []
        right = []

        left.append(1)
        right.append(1)

        for i in range(1, len(A)):
            left.append(left[-1] * A[i - 1])

        for i in range(len(A) - 2, -1, -1):
            right.insert(0, right[0] * A[i + 1])

        res = []

        for i in range(0, len(A)):
            res.append(left[i] * right[i])

        return res
