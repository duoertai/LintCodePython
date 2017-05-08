class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        if nums is None or len(nums) <= 1:
            return

        i = 0
        left = 0
        while i < len(nums):
            if nums[i] != 0:
                self.swap(nums, i, left)
                i += 1
                left += 1
            else:
                i += 1

        return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        return
