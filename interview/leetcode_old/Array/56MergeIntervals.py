# 56 Merge Intervals
# idea comes form https://leetcode.com/problems/merge-intervals/solution/
'''
Intuition

If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

Algorithm

First, we sort the list as described. Then, we insert the first interval into our merged list and continue considering each interval in turn as follows: If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to merged. Otherwise, they do overlap, and we merge them by updating the end of the previous interval if it is less than the end of the current interval.
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x : x.start)
        merge = []
        for interval in intervals:
            if not merge or merge[-1].end < interval.start:
                merge.append(interval)
            else:
                merge[-1].end = max(merge[-1].end, interval.end)
        return merge
