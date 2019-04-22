# Find K Nearest Point
# Leetcode 658 Find K Closest Elements
# Given a sorted array, two intergers k and x, find the k closest elements to x in the array.

# Using Binary Search and Two Pointers
# Time : O(logn + k)
# Space : O(k)
class Solution1(object):
	def findClosestElements(self, arr, k, x):
		n = len(arr)

		if x <= arr[0]:
			return arr[: k]
		elif x >= arr[-1]:
			return arr[len(arr) - k:]
		else:
			# use binary search find index of element (is equal to x or a little bit larger that x)
			# binary search
			ind = -1
			lo, hi = 0, n - 1
			while lo <= hi:
				mid = (lo + hi) / 2
				if arr[mid] >= x:
					hi = mid - 1
					ind = mid
				else:
					low = mid + 1

			# shrink the boundaries
			if ind < 0:
				ind = 0
			low = max(0, ind - k - 1)
			high = min(n - 1, ind + k - 1)
			while high - low > k - 1:
				if low < 0 or x - arr[low] <= arr[high] - x:
					high -= 1
				elif high > n or x - arr[low] > arr[high] - x:
					low += 1
				else:
					pass
			return arr[low: high + 1]

# Without using binary search
# binary-search for where the resulting elements start in the array
# https://leetcode.com/problems/find-k-closest-elements/discuss/106419/O(log-n)-Java-1-line-O(log(n)-%2B-k)-Ruby
class Solution2(object):
	def findClosestElements(self, arr, k, x):
		lo, hi = 0, len(arr) - k
		while lo < hi:
			mid = (lo + hi) / 2
			if x - arr[mid] > arr[mid + k] - x:
				lo = mid + 1
			else:
				hi = mid
		return arr[lo, lo + k]
