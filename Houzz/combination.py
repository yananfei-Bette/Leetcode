# combination
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=492795


"""
given:[
		['a', 'b', 'c'],
		['d'],
		['e', 'f']
	]
give: "ade", "adf", "bde", "bdf", "cde", "cdf"
memory cannot support all results.
a function next() will be called to output the next combination.
"""

class Solution1(object):
	def combination(self, lists):
		def permute(lists, curr, currId):
			if len(curr) == len(lists):
				res.append(curr)
				return

			for i in range(len(lists[currId])):
				permute(lists, curr + lists[currId][i], currId + 1)
			return

		res = []
		permute(lists, "", 0)
		return res


class Solution2(object):
	def __init__(self, lists):
		self.lists = lists
		self.marks = sum([len(l) - 1 for l in lists])
		self.lastVisited = False
		self.indes = [0] * len(lists)

	def next(self):
		if sum(self.indes) == self.marks and self.lastVisited:
			return None

		res = ""
		for r, c in enumerate(self.indes):
			res += self.lists[r][c]

		if sum(self.indes) == self.marks:
			self.lastVisited = True

		# change ind in indes, get the next permutation
		for r in range(len(self.indes) - 1, -1, -1):
			c = self.indes[r]
			if len(self.lists[r]) > 1:
				if len(self.lists[r]) - 1 > c:
					self.indes[r] += 1
					break
				elif len(self.lists[r]) - 1 == c and not self.lastVisited:
					self.indes[r] = 0
					continue
			elif len(self.lists[r]) == 1:
				continue

		return res

if __name__ == "__main__":
	lists = [['a', 'b', 'c'], ['d'], ['e', 'f']]
	sol1 = Solution1()
	print(sol1.combination(lists))

	sol2 = Solution2(lists)
	print(sol2.next())
	print(sol2.next())
	print(sol2.next())
	print(sol2.next())
	print(sol2.next())
	print(sol2.next())
	print(sol2.next())

