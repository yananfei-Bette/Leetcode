# Four Integer
# Given four integers, swap any two integers to make F(S) = abs(S[0] - S[1]) + abs(S[1] - S[2]) + abs(S[2] - S[3]) to be the largest.
# https://www.1point3acres.com/bbs/thread-202529-1-1.html

class Solution(object):
	def __init__(self):
		self.res = None

	def swap(self, i, j):
		self.res[i], self.res[j] = self.res[j], self.res[i]

	def fourIntegers(A, B, C, D):
		self.res = [A, B, C, D]
		self.res.sort()
		self.swap(0, 1)
		self.swap(2, 3)
		self.swap(0, 3)
		return self.res