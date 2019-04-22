# word Break
# leetcode 139


# https://leetcode.com/problems/word-break/solution/


class Solution1(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		# Brute Force
		# recusion and backtracking
		# Time: O(n ^ n)
		# Space: O(n)
		# TLE

		def backtrack(s, wordDict, ind):
			if ind == len(s):
				return True
			for i in range(ind, len(s)):
				if s[ind: i + 1] in wordDict and backtrack(s, wordDict, i + 1):
					return True
			return False
		
		return backtrack(s, set(wordDict), 0)



class Solution2(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		# Recursion with memorization
		# Time: O(n * n)
		# Space: O(n)

		def backtrack_memo(s, wordDic, ind, memo):
			if ind == len(s):
				return True
			if memo[ind] != None:
				return memo[ind]
			for i in range(ind, len(s)):
				if s[ind: i + 1] in wordDict and backtrack_memo(s, wordDict, i + 1, memo):
					memo[ind] = True
					return True
			memo[ind] = False
			return False
		
		return backtrack_memo(s, set(wordDict), 0, [None] * len(s))



class Solution3(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		# BFS
		# Time: O(n * n)
		# Space: O(n)

		wordDictSet = set(wordDict)
		queue = [0]
		visited = [0] * len(s)
		while queue:
			i = queue.pop(0)
			if visited[i] == 0:
				for j in range(i, len(s)):
					if s[i: j + 1] in wordDictSet:
						queue.append(j + 1)
						if j + 1 == len(s):
							return True
				visited[i] = 1
		return False



class Solution4(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		# DP
		# Time: O(n * n)
		# Space: O(n)

		wordDictSet = set(wordDict)
		dp = [False] * (len(s) + 1)
		dp[0] = True
		for i in range(1, len(s) + 1):
			for j in range(i):
				if dp[j] and s[j: i] in wordDictSet:
					dp[i] = True
					break
		return dp[-1]
		