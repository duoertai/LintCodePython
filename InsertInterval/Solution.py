"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """

    def insert(self, intervals, newInterval):
        results = []
        # write your code here

        if intervals is None or len(intervals) == 0:
            results.append(newInterval)
            return results

        i = 0

        while i < len(intervals) and intervals[i].end < newInterval.start:
            results.append(intervals[i])
            i += 1

        if i == len(intervals):
            results.append(newInterval)
            return results

        newInterval.start = min(newInterval.start, intervals[i].start)

        while i < len(intervals) and intervals[i].start <= newInterval.end:
            i += 1

        if i > 0:
            newInterval.end = max(intervals[i - 1].end, newInterval.end)

        results.append(newInterval)

        while i < len(intervals):
            results.append(intervals[i])
            i += 1

        return results
