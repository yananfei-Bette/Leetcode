# Search in Rotated Sorted Array
# leetcode 33

class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		def binarySearch(nums, target, lo, hi):
			if lo > hi:
				return -1
			mid = (lo + hi) / 2
			if nums[mid] == target:
				return mid
			
			if nums[lo] <= nums[mid]:
				# left part is sorted
				if nums[lo] <= target <= nums[mid]:
					return binarySearch(nums, target, lo, mid - 1)
				else:
					return binarySearch(nums, target, mid + 1, hi)
			else:
				if nums[mid] <= target <= nums[hi]:
					return binarySearch(nums, target, mid + 1, hi)
				else:
					return binarySearch(nums, target, lo, mid - 1)

		lo, hi = 0, len(nums) - 1
		return binarySearch(nums, target, lo, hi)
		