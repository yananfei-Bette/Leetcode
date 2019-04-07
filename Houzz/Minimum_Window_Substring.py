# Minimum Window Substring
# leetcode 76

class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		if not t:
			return ""
		
		dicT = collections.Counter(t)
		required = len(dicT)
		
		formed = 0
		windowCount = {}
		res = (float("inf"), None, None)
		l, r = 0, 0
		
		while r < len(s):
			char = s[r]
			windowCount[char] = windowCount.get(char, 0) + 1
			if char in dicT and windowCount[char] == dicT[char]:
				formed += 1
			
			while l <= r and formed == required:
				if r - l + 1 < res[0]:
					res = (r - l + 1, l, r)
				
				char = s[l]
				windowCount[char] -= 1
				# must notice here!!!!!
				# windowCount[char] < dictT[char]
				if char in dicT and windowCount[char] < dicT[char]:
					formed -= 1
				l += 1
			r += 1
		return "" if res[0] == float("inf") else s[res[1]: res[2] + 1]






		