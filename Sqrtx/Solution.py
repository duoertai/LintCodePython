class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x <= 0:
            return 0
        if x == 1:
            return 1

        left = 1
        right = x / 2

        while left < right:
            mid = left + (right - left) / 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid

            if mid * mid > x:
                right = mid - 1
            elif (mid + 1) * (mid + 1) <= x:
                left = mid + 1

        return left
