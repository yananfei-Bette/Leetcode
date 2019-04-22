# set Matrix zeroes
# leetcode 73

class Solution1(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		# additional memory approach
		# Time: O(m * n)
		# Space: O(m + n)
		
		rowSet = set()
		colSet = set()
		
		m = len(matrix)
		n = len(matrix[0])
		
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					rowSet.add(i)
					colSet.add(j)
		
		for i in range(m):
			for j in range(n):
				if i in rowSet or j in colSet:
					matrix[i][j] = 0
		
		return


class Solution2(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		# Brute force
		# Time: O(m * n * (m + n))
		# Space: O(1)
		
		MODIFIED = float("-inf")
		m = len(matrix)
		n = len(matrix[0])
		
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					for k in range(n):
						if matrix[i][k] != 0:
							matrix[i][k] = MODIFIED
					for k in range(m):
						if matrix[k][j] != 0:
							matrix[k][j] = MODIFIED
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == MODIFIED:
					matrix[i][j] = 0
		
		return


class Solution3(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		# flag
		# Time: O(m * n)
		# Space: O(1)
		is_col = False
		m = len(matrix)
		n = len(matrix[0])
		
		for i in range(m):
			if matrix[i][0] == 0:
				is_col = True
			for j in range(1, n):
				if matrix[i][j] == 0:
					matrix[i][0] = 0
					matrix[0][j] = 0
		
		for i in range(1, m):
			for j in range(1, n):
				if not matrix[i][0] or not matrix[0][j]:
					matrix[i][j] = 0
		
		if not matrix[0][0]:
			for j in range(n):
				matrix[0][j] = 0
		
		if is_col:
			for i in range(m):
				matrix[i][0] = 0
		
		return
		
		
		
		
		