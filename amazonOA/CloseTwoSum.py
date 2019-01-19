# Close Two Sum
# Find optimal weights

class Container(object):
	def __init__(self):
		self.first = None
		self.seconde = None

class Solution(object):
	def findOptimalWeights(self, capacity, weights, numOfContainers):
		minVal = 0.0
		minPos = 0
		maxPos = len(weights) - 1
		i, j = 0, len(weights) - 1

		weights.sort()

		while i < j:
			summ = weights[i] + weights[j]
			if summ > minVal and summ <= capacity:
				minVal = summ
				minPos = i
				maxPos = j

			if summ > capacity:
				j -= 1
			else:
				i += 1
		return [weights[minPos], weights[maxPos]]