class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        if A is None or len(A) == 0:
            return 0
        if len(A) == 1:
            if A[0] == elem:
                return 0
            else:
                return 1

        left = 0
        i = 0
        right = len(A) - 1

        while i < right:
            if A[i] == elem:
                self.swap(A, i, right)
                right -= 1
            else:
                i += 1

        if A[right] == elem:
            return right
        else:
            return right + 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        return
