class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        if A is None or len(A) <= 1:
            return

        for i in range(1, len(A)):
            j = i - 1
            temp = A[i]

            while j >= 0:
                if A[j] >= temp:
                    A[j + 1] = A[j]
                    j -= 1
                else:
                    break

            A[j + 1] = temp

        return