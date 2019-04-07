# sort array after converting elements to their squares
# https://www.geeksforgeeks.org/sort-array-converting-elements-squares/

# example 1
# input: arr = [-6, -3, -1, 2, 4, 5, 9]
# output: [1, 4, 9, 16, 25, 36, 81]

# solution 1
# time: O(n + nlogn)
class Solution1(object):
	def sortSquare(self, arr):
		# convert each element to square first
		# sort them
		for i in range(len(arr)):
			arr[i] *= arr[i]

		return sorted(arr)

# solution 2
# Time: O(nlogn)
class Solution2(object):
	def sortSquare(self, arr):
		# D and C
		# Divide the array into two part
		# Use merge function to merge two sorted array into a single sorted array.
		if not arr:
			return []

		return self.divideConquer(arr, 0, len(arr) - 1)

	def divideConquer(self, arr, i, j):
		if i == j:
			return [arr[i] * arr[i]]

		mid = (i + j) // 2
		l = self.divideConquer(arr, i, mid)
		r = self.divideConquer(arr, mid + 1, j)
		return self.merge(l, r)

	def merge(self, l, r):
		res = []
		while l and r:
			if l[0] < r[0]:
				res.append(l[0])
				l.pop(0)
			else:
				res.append(r[0])
				r.pop(0)
		return res + l if l else res + r

# solution 3
# Time: O(n)
class Solution3(object):
	def sortSquare(self, arr):
		# https://stackoverflow.com/questions/49542410/sorted-squares-of-numbers-in-a-list-in-on

		# take advantage of sorted arr

		# split it into 2 lists. One with negtive numbers, let's say list A.
		# One with positive numbers and 0, list B.
		# This is done while preserving the input order, which is trivial: O(n)

		# Reverse list A
		# Square every item of both lists in place : O(n)
		# Run merge operation needs: O(n)

		# Total: O(n)

		# split
		neg = []
		pos = []
		for i in range(len(arr)):
			if arr[i] < 0:
				neg.append(arr[i])
			else:
				pos.append(arr[i])

		# reverse and square
		if neg:
			neg = [e * e for e in neg[::-1]]
		if pos:
			pos = [e * e for e in pos]

		# merge
		res = []
		while neg and pos:
			if neg[0] < pos[0]:
				res.append(neg[0])
				neg.pop(0)
			else:
				res.append(pos[0])
				pos.pop(0)

		return res + neg if neg else res + pos





if __name__ == "__main__":
	arr = [-6, -3, -1, 2, 4, 5, 9]
	sol1 = Solution1()
	print(sol1.sortSquare(arr.copy()))

	sol2 = Solution2()
	print(sol2.sortSquare(arr.copy()))

	sol3 = Solution3()
	print(sol3.sortSquare(arr.copy()))

