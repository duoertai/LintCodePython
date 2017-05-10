class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        if A is None or len(A) <= 1:
            return

        self.quicksort(A, 0, len(A) - 1)
        return

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        left = start
        i = start
        right = end
        pivot = nums[end]

        while i <= right:
            if nums[i] < pivot:
                self.swap(nums, i, left)
                i += 1
                left += 1
            elif nums[i] == pivot:
                i += 1
            else:
                self.swap(nums, i, right)
                right -= 1

        self.quicksort(nums, start, left - 1)
        self.quicksort(nums, right + 1, end)
        return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return
