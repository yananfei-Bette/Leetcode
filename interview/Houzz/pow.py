# pow(x, n)
# leetcode 50

class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		# brute force

		def multiply(x, n):
			res = 1
			for i in xrange(1, n + 1):
				res *= x
			return res
			
		mark = 0
		if n < 0:
			mark = 1
			n = -n
		return multiply(x, n) if mark == 0 else 1.0/multiply(x, n)

class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		# recursive

		def helper(x, n):
			if n == 0:
				return 1
			res = helper(x, n / 2)
			if n % 2 == 0:
				return res * res
			else:
				return res * res * x
			
		mark = 0
		if n < 0:
			mark = 1
			n = -n
		return helper(x, n) if mark == 0 else 1.0 / helper(x, n)


class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		# iterative
		mark = 0
		if n < 0:
			mark = 1
			n = -n
			
		res = 1
		curr = x
		i = n
		
		while i > 0:
			if i % 2 == 1:
				res *= curr
			curr *= curr
			i /= 2
		return res if mark == 0 else 1.0 / res