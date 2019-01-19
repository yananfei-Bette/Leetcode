# Rotate Matrix
# Leetcode 48 Rotate Image

class Solution48(object):
	def rotate(self, matrix):
		if not matrix:
			return matrix
		n = len(matrix[0])
		for i in range(n // 2 + n % 2):
			for j in range(n // 2):
				tmp = [0] * 4
				row, col = i, j
				for k in range(4):
					tmp[k] = matrix[row][col]
					row, col = col, n - 1 - row
				for k in range(4):
					matrix[row][col] = tmp[(k - 1) % 4]
					row, col = col, n - 1 - row

class Solution(object):
	def rotate(self, matrix, flag):
		if not matrix:
			return matrix

		m = len(matrix)
		n = len(matrix[0])

		res = [[0] * n for _ in range(m)]

		for i in range(m):
			for j in range(n):
				res[i][j] = matrix[i][j]

		if flag == 1:
			for i in range(m):
				for j in range(n / 2):
					# swap
					matrix[i][j] ^= matrix[i][n - j - 1]
					matrix[i][n - j - 1] ^= matrix[i][j]
					matrix[i][j] ^= matrix[i][n - j - 1]
		else:
			for i in range(m / 2):
				for j in range(n):
					# swap
					matrix[i][j] ^= matrix[m - i - 1][j]
					matrix[m - i - 1][j] ^= matrix[i][j]
					matrix[i][j] ^= matrix[m - i - 1][j]

		return res