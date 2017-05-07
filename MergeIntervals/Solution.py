
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if intervals is None or len(intervals) <= 1:
            return intervals

        res = []

        def cmp(i1, i2):
            if i1.start < i2.start:
                return -1
            elif i1.start > i2.start:
                return 1
            else:
                return 0

        intervals = sorted(intervals, cmp)

        temp = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i].start > temp.end:
                res.append(temp)
                temp = intervals[i]
            else:
                temp.end = max(temp.end, intervals[i].end)
        res.append(temp)

        return res
