# Greatest Common Divisor
# Given an array, find the GCD of those numbers in this array
# http://www.voidcn.com/article/p-ewiwfcye-hw.html

class Solution(object):
	def GCD(self, arr):
		if not arr:
			return 0
		if len(arr) < 2:
			return arr[0]

		res = arr[0]
		for i in range(1, len(arr)):
			if arr[i] > 0 and res > 0:
				res = self.GCDfind(res, arr[i])
			else:
				return 0
		return res

	def GCDfind(self, num1, num2):
		if num1 % num2 == 0:
			return num2
		else:
			return self.GCDfind(num2, num1 % num2)

