class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if A is None:
            return B
        if B is None:
            return A

        m = len(A)
        n = len(B)
        l = m + n
        i = 0
        j = 0
        res = []

        for k in range(0, l):
            num1 = sys.maxint
            if i < m:
                num1 = A[i]

            num2 = sys.maxint
            if j < n:
                num2 = B[j]

            if num1 < num2:
                res.append(num1)
                i += 1
            else:
                res.append(num2)
                j += 1

        return res
