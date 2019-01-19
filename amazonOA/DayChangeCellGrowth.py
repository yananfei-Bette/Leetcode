# Day change (cell growth)
class Solution(object):
	def cellGrowth(self, cells, days):
		if not cells or days <= 0:
			return cells
		n = len(cells)
		res = [0] * (n + 2)

		for i in range(1, n + 1):
			res[i] = cells[i - 1]

		for i in range(days):
			prev = res[0]
			for j in range(1, n + 1):
				prev, res[j] = res[j], prev ^ res[j + 1]
		return res[1: n + 1]

if __name__ == "__main__":
	res = Solution()
	cells = [1, 1, 1, 0, 1, 1, 1, 1]
	days = 2
	print(res.cellGrowth(cells, days))