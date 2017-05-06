class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        if nums1 is None or len(nums1) == 0 or nums2 is None or len(nums2) == 0:
            return []

        res = []
        map1 = {}

        for n in nums1:
            if not map1.has_key(n):
                map1[n] = 1
            else:
                map1[n] = map1[n] + 1

        for n in nums2:
            if map1.has_key(n) and map1[n] > 0:
                res.append(n)
                map1[n] -= 1

        return res
