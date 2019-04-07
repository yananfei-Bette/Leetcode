# wildchard Matching
# leetcode 44


class Solution1(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		# recursion top-down
		# TEL

		if not p:
			return not s
		if not s:
			return p.count("*") == len(p)
		if p[0] in {"?", s[0]}:
			return self.isMatch(s[1:], p[1:])
		if p[0] == "*":
			return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
		return False



class Solution2(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		# resursion with memo
		memo = {}
		def dfs(i, j):
			if (i, j) in memo:
				return memo[(i, j)]
			res = False
			if j == len(p):
				res = i == len(s)
			elif i == len(s):
				res = p[j:].count("*") == len(p[j:])
			elif p[j] in {s[i], "?"}:
				res = dfs(i + 1, j + 1)
			elif p[j] == "*":
				res = dfs(i, j + 1) or dfs(i + 1, j)
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
		# buttom up
		dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
		dp[-1][-1] = True
		
		for i in range(len(s), -1, -1):
			for j in range(len(p) - 1, -1, -1):
				if i == len(s):
					dp[i][j] = p[j:].count("*") == len(p[j:])
				elif p[j] in {s[i], "?"}:
					dp[i][j] = dp[i + 1][j + 1]
				elif p[j] == "*":
					dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
		return dp[0][0]
		