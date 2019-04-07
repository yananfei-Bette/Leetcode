# leetcode 767
# reorganize string
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=470555

class Solution(object):
	def recoganizeString1(self, S):
		# Sort by Count
		# Time: O(n + aloga)
		# Space: O(n + a)
		N = len(S)
		A = []
		for c, x in sorted((S.count(x), x) for x in set(S)):
			if c > (N + 1) / 2:
				return ""
			A.extend(c * x)

		res = [None] * N
		res[::2], N[1::2] = A[N / 2:], A[: N / 2]
		return "".join(res)


	def recoganizeString2(self, S):
		# Greedy with heap
		# Time: O(nloga)
		# Space: O(a)
		minheap = []
		N = len(S)
		for x in set(S):
			c = S.count(x)
			if c > (N + 1) / 2:
				return ""
			heapq.heappush(minheap, (-c, x))

		res = []
		while len(minheap) >= 2:
			nc1, x1 = heapq.heappop(minheap)
			nc2, x2 = heapq.heappop(minheap)

			res.extend([x1, x2])

			if nc1 + 1 != 0:
				heapq.heappush((nc1 + 1, x1))
			if nc2 + 1 != 0:
				heapq.heappush((nc2 + 1, x2))

		return "".join(res) + minheap[0][1] if minheap else ""
