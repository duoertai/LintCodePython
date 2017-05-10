class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """

    def minimumTotal(self, triangle):
        # write your code here
        if triangle is None or len(triangle) == 0 or triangle[0] is None or len(triangle[0]) == 0:
            return 0

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
