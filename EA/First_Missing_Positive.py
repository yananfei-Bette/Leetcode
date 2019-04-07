# First Missing Positive
# leetcode 41
# good problem!!!!!!

class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# busket sort
		# index [0, 1, 2, 3]
		# arr   [1, 2, 3, 4]
		# https://www.youtube.com/watch?v=jfb72FfxWKU
		# time: O(n)
		# space: O(1)

		if not nums:
			return 1
		
		for i in range(len(nums)):
			while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
				# swap
				temp = nums[nums[i] - 1]
				nums[nums[i] - 1] = nums[i]
				nums[i] = temp
		
		for i in range(len(nums)):
			if nums[i] != i + 1:
				return i + 1
		return len(nums) + 1