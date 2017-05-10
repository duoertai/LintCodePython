class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        if A is None or len(A) <= 1:
            return

        self.mergesort(A, 0, len(A) - 1)
        return

    def mergesort(self, nums, start, end):
        if start >= end:
            return

        mid = start + (end - start) / 2
        self.mergesort(nums, start, mid)
        self.mergesort(nums, mid + 1, end)
        self.merge(nums, start, mid, end)
        return

    def merge(self, nums, start, mid, end):
        part1 = []
        part2 = []

        for i in range(0, mid - start + 1):
            part1.append(nums[start + i])
        for i in range(0, end - mid):
            part2.append(nums[mid + 1 + i])

        p1 = 0
        p2 = 0
        i = 0

        while p1 < len(part1) or p2 < len(part2):
            num1 = sys.maxint
            if p1 < len(part1):
                num1 = part1[p1]

            num2 = sys.maxint
            if p2 < len(part2):
                num2 = part2[p2]

            if num1 < num2:
                nums[start + i] = num1
                p1 += 1
            else:
                nums[start + i] = num2
                p2 += 1

            i += 1

        return
