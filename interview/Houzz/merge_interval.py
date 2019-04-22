# merge interval
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=485395

class Interval(object):
	def __init__(self, s = 0, e = 0):
		self.start = s
		self.end = e


# leetcode 56
# merge interval
class Solution1(object):
	def merge(self, intervals):
		intervals.sort(key = lambda x: x.start)
		res = []
		for i in intervals:
			if not res or res[-1].end < i.start:
				res.append(i)
			else:
				res[-1].end = max(res[-1].end, i.end)
		return res


# leetcode 57
# insert interval
class Solution2(object):
	def insert(self, intervals, newInterval):
		res = []
		i = 0
		while i < len(intervals) and intervals[i].end < newInterval.start:
			res.append(intervals[i])
			i += 1

		while i < len(intervals) and intervals[i].start < newInterval.end:
			newInterval = Interval(min(intervals[i].start, newInterval.start),
									max(intervals[i].end, newInterval.end))
			i += 1
		res.append(newInterval)


		while i < len(intervals):
			res,append(intervals[i])
			i += 1

		return res


# leetcode 253
# Meeting room
class Solution3(object):
	def minMeetingRooms(self, intervals):
		if not intervals:
			return 0
		minheap = []
		intervals.sort(key = lambda x: x.start)
		for i in intervals:
			if minheap and minheap[0] < i.start:
				heapq.heappop(minheap)
			heapq.heappush(minheap, i.end)
		return len(minheap)


# leetcode 495
# Teemo Attacking
class Solution4(object):
	def findPosionedDuration(self, timeSeries, duration):
		res = 0
		if not timeSeries:
			return res
		for i in range(1, len(timeSeries)):
			res += min(duration, timeSeries[i] - timeSeries[i - 1])
		res += duration
		return res


# leetcode 759
# Employee Free Time
class Solution5(object):
	def employeeFreeTime1(self, schedule):
		# events with balance record
		# Time: O(clogc)
		# Space: O(c)
		OPEN, CLOSE = 0, 1
		events = []
		for emp in schedule:
			for interval in emp:
				events.append((interval.start, OPEN))
				events.append((interval.end, CLOSE))

		events.sort()

		res = []
		prev = None
		balance = 0
		for t, cmd in enumerate(events):
			if balance == 0 and prev != None:
				res.append(Interval(prev, t))

			balance += 1 if cmd == OPEN else -1
			prev = t

		return res


	def employeeFreeTime2(self, schedule):
		# My method
		# extend all interrvals, sort them and found free time
		intervals = []
		for emp in schedule:
			for interval in emp:
				intervals.append(interrval)

		interval.sort(key = lambda x: x.start)
		mergedIntervals = []
		for interval in intervals:
			if not mergedIntervals or mergedIntervals[-1].end < interval.start:
				mergedIntervals.append(interval)
			else:
				mergedIntervals[-1].end = max(mergedIntervals[-1], interval.end)

		res = []
		for i in range(1, len(mergedIntervals)):
			res.append(Interval(mergedIntervals[i - 1].end, mergedIntervals[i].start))

		return res


	def employeeFreeTime3(self, schedule):
		# priority queue
		# it kinds of like merge k linked list
		res = []
		minheap = []
		for ei, emp in enumerate(schedule):
			heapq.heappush((emp[0].start, ei, 0))

		anchor = min(interval.start for emp in schedule for interval in emp)

		while minheap:
			t, ei, ej = heapq.heappop(minheap)
			if anchor < t:
				res.append(Interval(anchor, t))
			anchor = max(anchor, schedule[ei][ej].end)
			if ej + 1 < len(schedule[ei]):
				heapq.heappush((schedule[ei][ej + 1].start, ei, ej + 1))
		return res



















