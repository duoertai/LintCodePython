class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        sum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if sum > 0:
                sum = 0
            sum += nums[i]
            res = min(res, sum)

        return res
