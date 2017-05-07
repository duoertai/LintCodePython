class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        sum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if sum < 0:
                sum = 0

            sum += nums[i]
            res = max(res, sum)

        return res
