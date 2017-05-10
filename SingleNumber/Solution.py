class Solution:
    """
    @param A : an integer array
    @return : a integer
    """

    def singleNumber(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        res = A[0]
        for i in range(1, len(A)):
            res = res ^ A[i]

        return res
