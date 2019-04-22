# Arithmetic Sequence
# Given an array, return the numberof all possible arithmetic sequence.
# Leetcode 413

class Solution1(object):
	# Time: O(n)
	# Space: O(1)
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
        	return 0

        res = 0
        diff = float("inf")
        count = 0
        start = 0

        for i in range(1, len(A)):
        	currDiff = A[i] - A[i - 1]
        	if diff == currDiff:
        		count += i - start - 1 if i - start - 1 > 0 else 0
        	else:
        		start = i - 1
        		diff = currDiff
        		res += count
        		count = 0
        res += count
        return res

# DP
class Solution2(object):
	def numberOfArithmeticSlices(self, A):
		if not A or len(A) < 3:
			return 0
		count = 0
		dp = [0] * len(A)
		for i in range(len(A) - 2):
			if A[i] - A[i + 1] == A[i + 1] - A[i + 2]:
				dp[i + 2] = 1 + dp[i + 1]
				count  += dp[i + 2]
		return count

