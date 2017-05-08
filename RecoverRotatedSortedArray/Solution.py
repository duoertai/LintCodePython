class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return

        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1

        if i == len(nums) - 1:
            return

        self.reverse(nums, 0, i)
        self.reverse(nums, i + 1, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

        return

    def reverse(self, nums, left, right):
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1

        return

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return
