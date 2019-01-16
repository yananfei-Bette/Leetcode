# Window Sum
# https://www.jianshu.com/p/3d98e7b046aa

# Given array: [1, 2, 3, 4, 5, 6, 7]
# Given window size: 3
# Output: [6, 9, 12, 15, 18]

# Time : O(n * n)
# Space: O(n)
class Solution1(object):
	def sumOfWindow(self, arr, k):
		res = []
		if not arr or k <= 0:
			return []
		count = 0
		for i in range(len(arr)):
			count += 1
			if count >= k:
				summ = 0
				for j in range(i, i - k, -1):
					summ += arr[j]
				res.append(summ)
		return res

# Time: O(n)
# Space: O(n)
class Solution2(object):
	def sumOfWindow(self, arr, k):
		if not arr or k <= 0:
			return []
		res = [0] * len(arr)
		for i in range(k):
			res[0] += arr[i]
		for i in range(k, len(arr) - k):
			res[i] = res[i - 1] - arr[i - 1] + arr[i + k - 1]
		return res