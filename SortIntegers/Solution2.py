class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        if A is None or len(A) <= 1:
            return

        for i in range(0, len(A)):
            for j in range(0, len(A) - i - 1):
                if A[j] > A[j + 1]:
                    temp = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = temp

        return
