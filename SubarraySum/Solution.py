class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []

        res = []
        map = {}
        sum = 0

        map[sum] = 0

        for i in range(1, len(nums)):
            sum += nums[i - 1]

            if map.has_key(sum):
                res.append(map[sum])
                res.append(i - 1)
                return res
            else:
                map[sum] = i

        sum += nums[len(nums) - 1]
        res.append(map[sum])
        res.append(len(nums) - 1)

        return res
