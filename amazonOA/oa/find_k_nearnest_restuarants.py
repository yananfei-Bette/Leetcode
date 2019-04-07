# find k nearnest restuarants
# http://jingyid.me/2018/07/19/Amazon-OA2-Practice/
# https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute

import heapq

class Solution(object):
	def __init__(self):
		self.origin = None

	def kClosest(self, points, origin, k):
		self.origin = origin

		minheap = []
		res = []
		for p in points:
			heapq.heappush(minheap, (-self.getDist(p), p[0], p[1], p))
			if len(minheap) > k:
				heapq.heappop(minheap)

		for loc in minheap:
			res.append(loc[3])
		return res

	def getDist(self, p):
		return (p[0] - self.origin[0]) ** 2 + (p[1] - self.origin[1]) ** 2


if __name__ == "__main__":
	points = [[1, -3], [1, 2], [3, 4], [4, 3]]
	origin = [0, 0]
	k = 3
	sol = Solution()
	print(sol.kClosest(points, origin, k))