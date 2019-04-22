# 253 Meeting rooms ii
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # corner case
        # notice, egded condition <=
        if not intervals:
            return 0

        minheap = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval.end)
        return len(minheap)