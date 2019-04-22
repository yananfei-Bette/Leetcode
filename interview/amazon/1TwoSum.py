# Two Sum
# Leetcode 1

# Brute Force
# Time: O(n * n)
# Space: O(1)
class Solution1(object):
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]
		return []

# Two-pass solution
# The first pass creates index dic
# Time: O(2 * n)
# Space: O(n)
class Solution2(object):
	def twoSum(self, nums, target):
		dic = {}
		for i in range(len(nums)):
			dic[nums[i]] = dic.get(nums[i], []) + [i]

		for i in range(len(nums)):
			x = target - nums[i]
			if x in dic:
				for ind in dic[x]:
					if ind != i:
						return [i, ind]
		return []

# One pass
# Time: O(n)
# Space: O(n)
class Solution3(object):
	def twoSum(self, nums, target):
		dic = {}
		for i in range(len(nums)):
			x = target - nums[i]
			if x in dic:
				return [dic[x], i]
			else:
				dic[nums[i]] = i
		return []
