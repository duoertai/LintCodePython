class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """

    def median(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) % 2 == 1:
            return self.quickselect(nums, 0, len(nums) - 1, len(nums) / 2)
        else:
            return self.quickselect(nums, 0, len(nums) - 1, len(nums) / 2 - 1)

    def quickselect(self, nums, start, end, k):
        if (start > end):
            return 0

        left = start
        i = start
        right = end
        pivot = nums[end]

        while i <= right:
            if nums[i] < pivot:
                self.swap(nums, i, left)
                i += 1
                left += 1
            elif nums[i] > pivot:
                self.swap(nums, i, right)
                right -= 1
            else:
                i += 1

        if left <= k and k <= right:
            return nums[k]
        elif k < left:
            return self.quickselect(nums, start, left - 1, k)
        else:
            return self.quickselect(nums, right + 1, end, k)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        return
