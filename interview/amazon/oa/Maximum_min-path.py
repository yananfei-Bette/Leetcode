# Maximum min-path

"""
You are gonna climb mountains represented by a matrix. Each integer in the matrix represents the altitude at that point. You are supposed to climb from the top-left corner to the bottom-right corner and only move rightward or downward in each step.
You can have many paths to do so. Each path has a minimum altitude. Find the maximum among all the minimum altitudes of all paths.
e.g. 545136
 
Three paths: 5 1 3 6，5 4 3 6，5 4 5 6. Minimums are 1, 3, 4 respectively. Return the maximum in them which is 4.
another example:
 
[8, 4, 7]
[6, 5, 9]
3 paths: 8-4-7-9 min: 4 8-4-5-9 min: 4 8-6-5-9 min: 5 return: 5
"""

# dfs
class Solution1(object):
	def __init__(self):
		self.min = float("inf")
		self.max = float("-inf")
		self.row = None
		self.col = None

	def maxMinPath(self, matrix):
		if not matrix or not matrix[0]:
			return -1

		self.row = matrix
		self.col = matrix[0]

		self.dfs(matrix, 0, 0)
		return self.max

	def dfs(matrrix, i, j):
		if i >= self.row or j >= self.col:
			return

		if i == self.row - 1 and j == self.col - 1:
			self.min = min(self.min, matrix[i][j])
			self.max = max(self.min, self.max)

		self.min = min(self.min, matrix[i][j])
		self.dfs(matrix, i, j + 1)
		self.dfs(matrix, i + 1, j)
		return



# dp
# leetcode 174
class Solution2(object):
	def maxMinPath(self, matrix):
		if not matrix or not matrix[0]:
			return -1

		m = len(matrix)
		n = len(matrix[0])

		dp = [0] * n
		dp[0] = matrix[0][0]

		for i in range(1, n):
			dp[i] = min(dp[i - 1], matrix[0][i])


		for i in range(1, m):
			dp[0] = max(matrix[i][0], dp[0])
			for j in range(1, n):
				if dp[j] < matrix[i][j] and dp[j - 1] < matrix[i][j]:
					dp[j] = max(dp[j - 1], dp[j])
				else:
					dp[j] = matrix[i][j]
		return dp[-1]
