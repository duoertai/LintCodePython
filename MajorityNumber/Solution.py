class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if res == nums[i]:
                count += 1
            else:
                count -= 1
                if count < 0:
                    res = nums[i]

        return res
