# two sum Closet
# closeset two sum < target, return pair
# car with package

class Solution(object):
	def twoSum(numbers, target):
		numbers.sort()
		lo, hi = 0, len(numbers) - 1
		minDiff = float("inf")
		res = [None, None]

		while lo < hi:
			curr = numbers[lo] + numbers[hi]
			currDiff = target - curr:
			if 0 <= currDiff < minDiff:
				minDiff = currDiff
				res[0] = numbers[lo]
				res[1] = numbers[hi]

			if curr < target:
				lo += 1
			else:
				hi -= 1
		return res if res[0] != None else -1