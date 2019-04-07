# word Break 2
# leetcode 140


class Solution1(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		# bcaktrack
		# Time: O(n ^ n)
		# space: O(n * n * n)

		def backtrack(s, wordDict, start):
			res = []
			
			if start == len(s):
				res.append("")
				return res
			
			for i in range(start, len(s)):
				if s[start: i + 1] in wordDict:
					lists = backtrack(s, wordDict, i + 1)
					for l in lists:
						res.append(s[start: i + 1] + ("" if l == "" else " ") + l)
			return res
						
		return backtrack(s, set(wordDict), 0)



class Solution2(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rty
		"""
		# backtrack with memo
		# Time: O(n ^ 3)
		# space: O(n ^ 3)
		
		def backtrack_memo(s, wordDict, start, memo):
			if start in memo:
				return memo[start]
			res = []
			if start == len(s):
				res.append("")
				return res
			for i in range(start, len(s)):
				if s[start: i + 1] in wordDict:
					lists = backtrack_memo(s, wordDict, i + 1, memo)
					for l in lists:
						res.append(s[start: i + 1] + ("" if l == "" else " ") + l)
			memo[start] = res
			return res
		
		return backtrack_memo(s, set(wordDict), 0, {})



class Solution3(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""		
		# DP
		# Time: O(n ^ 3)
		# Space: O(n ^ 3)
		# MLE

		dp = {i:[] for i in range(len(s) + 1)}
		dp[0].append("")
		wordDictSet = set(wordDict)
		
		for i in range(1, len(s) + 1):
			lists = []
			for j in range(i):
				if len(dp[j]) > 0 and s[j: i] in wordDictSet:
					for l in dp[j]:
						lists.append(l + ("" if l == "" else " ") + s[j: i])
			dp[i] = lists
		return dp[len(s)]

		

 