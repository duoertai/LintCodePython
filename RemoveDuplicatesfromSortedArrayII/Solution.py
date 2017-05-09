class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        slow = 1
        fast = 1
        count = 1

        for fast in range(1, len(A)):
            if A[fast] == A[fast - 1]:
                if count == 1:
                    count += 1
                    A[slow] = A[fast]
                    slow += 1
            else:
                A[slow] = A[fast]
                slow += 1
                count = 1

        return slow
