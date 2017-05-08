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

        while fast < len(A):
            while fast < len(A) and A[fast] == A[fast - 1]:
                fast += 1

            if fast == len(A):
                break

            A[slow] = A[fast]
            slow += 1
            fast += 1

        return slow
