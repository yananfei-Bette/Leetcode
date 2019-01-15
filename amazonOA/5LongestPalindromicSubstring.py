# Longest palindromic substring
# leetcode 5
# DP
def longestPalindrome(s):
	if not s:
		return ""
	res = ""
	maxLen = 0
	dp = [[False] * len(s) for _ in range(len(s))]

	for j in range(len(s)):
		for i in range(j + 1):
			dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
			if dp[i][j] and j - i + 1 > maxLen:
				maxLen = j - i + 1
				res = s[i : j + 1]
	return res

# recursive
class Solution(object):
	def __init__(self):
		self.res = ""

	def longestPalindrome(s):
		if not s:
			return ""

		for i in range(len(s)):
			self.helper(s, i, i)
			self.helper(s, i, i + 1)
		return self.res

	def helper(s, i, j):
		while 0 <= i <= j < len(s) and s[i] == s[j]:
			i -= 1
			j += 1

		i += 1
		j -= 1

		if j - i + 1 > len(self.res):
			self.res = s[i : j + 1]
		return