# Maximum the minimum Paths
# Given a mtrix, a path starts from top-left to down-right. The value of a path is minVal of those numbers which are on the path.
# Return the maximum value of those paths

# Matrix:
# [8, 4, 7]
# [6, 5, 9]
# Paths:
# 8-4-7-9, min: 4
# 8-4-5-9, min: 4
# 8-6-5-9, min: 5
# return 5

# DP
class Solution1(object):
	def MaxMinPath(self, matrix):
		res = [0] * len(matrix[0])
		res[0] = matrix[0][0]
		for i in range(1, len(matrix[0])):
			res[i] = min(res[i - 1], matrix[0][i])

		for i in range(1, len(matrix)):
			res[0] = min(matrix[i][0], res[0])
			for j in range(1, len(matrix[0])):
				if res[j] < matrix[i][j] and res[j - 1] < matrix[i][j]:
					res[j] = max(res[j], res[j - 1])
				else:
					res[j] = matrix[i][j]
		return res[-1]

# DFS
class Solution2(object):
	def __init__(self):
		self.row = None
		self.col = None
		self.min = float("inf")
		self.max = float("-inf")

	def MaxMinPath(self, matrix):
		self.row = len(matrix)
		self.col = len(matrix[0])
		self.dfs(matrix, 0, 0)
		return self.max

	def dfs(self, matrix, i, j):
		if i >= self.row or j >= self.col:
			return
		if i == self.row - 1 and j == self.col - 1:
			self.min = min(self.min, matrix[i][j])
			self.max = max(self.max, self.min)
			return
		self.min = min(self.min, matrix[i][j])
		self.dfs(matrix, i, j + 1)
		self.dfs(matrix, i + 1, j)
		return


