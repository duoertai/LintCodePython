class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # selection sort

        if A is None or len(A) <= 1:
            return

        for i in range(0, len(A)):
            min = i
            for j in range(i + 1, len(A)):
                if A[j] < A[min]:
                    min = j;

            temp = A[i]
            A[i] = A[min]
            A[min] = temp

        return
