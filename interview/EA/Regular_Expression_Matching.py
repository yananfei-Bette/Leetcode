# Regular Expression Matching
# leetcode 10


class Solution1(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		# recursion
		
		if not p:
			return not s
		firstMatch = bool(s) and p[0] in {s[0], '.'}
		if len(p) >= 2 and p[1] == "*":
			return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
		return firstMatch and self.isMatch(s[1:], p[1:])



class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
		# recursion with memo, top-down

		memo = {}
		def dfs(i, j):
			if (i, j) in memo:
				return memo[(i, j)]
			res = False
			if j == len(p):
				res = i == len(s)
			else:
				firstMatch = i < len(s) and p[j] in {s[i], "."}
				if j + 1 < len(p) and p[j + 1] == "*":
					res = dfs(i, j + 2) or (firstMatch and dfs(i + 1, j))
				else:
					res = firstMatch and dfs(i + 1, j + 1)
			memo[(i, j)] = res
			return res
		
		return dfs(0, 0)



class Solution3(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
		# buttom-up
		dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
		dp[-1][-1] = True
		
		for i in range(len(s), -1, -1):
			for j in range(len(p) - 1, -1, -1):
				firstMatch = i < len(s) and p[j] in {s[i], "."}
				if j + 1 < len(p) and p[j + 1] == "*":
					dp[i][j] = dp[i][j + 2] or (firstMatch and dp[i + 1][j])
				else:
					dp[i][j] = firstMatch and dp[i + 1][j + 1]
		return dp[0][0]