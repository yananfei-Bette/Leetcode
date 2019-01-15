# Find K Nearest Point
# Leetcode 658 Find K Closest Elements
# Given a sorted array, two intergers k and x, find the k closest elements to x in the array.

# Using Binary Search and Two Pointers
# Time : O()
# Space : O()
class Solution(object):
	def findClosestElements(self, arr, k, x):
		if x <= arr[0]:
			return arr[:k]
		elif x >= arr[-1]:
			return arr[len(arr) - 1 - k:]
		else:
			# use binary search find index of element (is equal to x or a little bit larger that x)
			
