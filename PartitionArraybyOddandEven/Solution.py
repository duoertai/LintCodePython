class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return

        left = 0
        i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] % 2 == 1:
                self.swap(nums, i, left)
                i += 1
                left += 1
            else:
                self.swap(nums, i, right)
                right -= 1

        return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        return
