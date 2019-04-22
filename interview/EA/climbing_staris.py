# climbing staris
# leetcode 70

class Solution1(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# dp
		# Time: O(n)
		# Space: O(n)
		if n == 1 or n == 2:
			return n
		dp = [0] * (n + 1)
		dp[1] = 1
		dp[2] = 2
		for i in range(3, n + 1):
			dp[i] = dp[i - 1] + dp[i - 2]
		return dp[-1]


class Solution2(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# reduce space complexity
		# Time: O(n)
		# Space: O(1)
		if n == 1 or n == 2:
			return n
		f1, f2 = 1, 2
		for _ in range(3, n + 1):
			f1, f2 = f2, f1 + f2
		return f2


class Solution3(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# Binet's Method
		# mathmatition formula
		# https://artofproblemsolving.com/wiki/index.php?title=Binet%27s_Formula
		# Time: O(1)
		# Space: O(1)
		sqrt5 = math.sqrt(5)
		fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
		return int(fibn / sqrt5)


class Solution4(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# Binets method
		# matrix
		# https://artofproblemsolving.com/community/c1157h990742_a_matrix_derivation_of_binets_formula
		# https://leetcode.com/problems/climbing-stairs/solution/
		# Time: O(logn)

		def matrixPow(Q, n):
			res = [[1, 0], [0, 1]]
			while n > 0:
				if (n & 1) == 1:
					res = multiply(res, Q)
				n >>= 1
				Q = multiply(Q, Q)
			return res

		def multiply(a, b):
			c = [[0] * 2 for _ in range(2)]
			for i in range(2):
				for j in range(2):
					c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
			return c

		Q = [[1, 1], [1, 0]]
		res = matrixPow(Q, n)
		return res[0][0]











