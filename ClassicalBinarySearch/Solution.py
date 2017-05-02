class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        if A is None or len(A) == 0:
            return -1

        if target < A[0] or target > A[len(A) - 1]:
            return -1

        left = 0
        right = len(A) - 1

        while left <= right:
            mid = left + (right - left) / 2

            if A[mid] == target:
                return mid

            if A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1