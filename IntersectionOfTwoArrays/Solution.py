class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        if nums1 is None or len(nums1) == 0 or nums2 is None or len(nums2) == 0:
            return []

        res = []
        set1 = set()
        set2 = set()

        for num in nums1:
            set1.add(num)

        for num in nums2:
            if num in set1 and num not in set2:
                res.append(num)
            set2.add(num)

        return res
