# 253 Meeting Rooms II

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
        # time: O(n*logn)
        # greedy with heap
        if not intervals:
            return 0
        minheap = []
        intervals.sort(key = lambda x: x.start)
        heapq.heappush(minheap, intervals[0].end)
        for i in intervals[1:]:
            if minheap[0] <= i.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)
        return len(minheap)