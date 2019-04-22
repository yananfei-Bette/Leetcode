# Search in 2D matrix
# Leetcode 74

class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            r = mid / n
            c = mid % n
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

class Solution2(object):
	def searchMatrix(self, matrix, target):
		if not matrix or not matrix[0]:
			return False
		if target < matrix[0][0] or target > matrix[-1][-1]:
			return False

		m = len(matrix)
		n = len(matrix[0])

		r = 0
		c = n - 1
		while r < m and c >= 0:
			if matrix[r][c] == target:
				return True
			elif matrix[r][c] > target:
				c -= 1
			else:
				r += 1
		return False
        