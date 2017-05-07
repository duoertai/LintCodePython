class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        index = m + n - 1
        i = m - 1
        j = n - 1

        for k in range(0, m + n):
            num1 = -sys.maxint - 1
            if i >= 0:
                num1 = A[i]

            num2 = -sys.maxint - 1
            if j >= 0:
                num2 = B[j]

            if num1 > num2:
                A[index] = num1
                i -= 1
                index -= 1
            else:
                A[index] = num2
                j -= 1
                index -= 1

        return
