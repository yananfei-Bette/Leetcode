# smallest window

# similiary question
# leetcode 76
# example 1:
# input: S = "ADOBECODEBANC", T = "ABC"
# output: "BANC"

class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		# use dic and two pointers
		if not t:
			return ""

		import collections

		dicT = collections.Counter(t)
		required = len(dicT)
		
		formed = 0
		windowCount = {}
		res = (float("inf"), None, None)
		l, r = 0, 0
		
		while r < len(s):
			# move r
			char = s[r]
			windowCount[char] = windowCount.get(char, 0) + 1
			if char in dicT and windowCount[char] == dicT[char]:
				formed += 1
			
			# if satisfied
			# record and remove l
			while l <= r and formed == required:
				if r - l + 1 < res[0]:
					res = (r - l + 1, l, r)
				
				char = s[l]
				windowCount[char] -= 1
				if char in dicT and windowCount[char] < dicT[char]:
					formed -= 1
				l += 1
			r += 1
		return "" if res[0] == float("inf") else s[res[1]: res[2] + 1]


if __name__ == "__main__":
	s = "ADOBECODEBANC"
	t = "ABC"
	sol = Solution()
	print(sol.minWindow(s, t))





