# Minimum Window Subsequence
# leetcode 727

"""
Approach #2: Dynamic Programming (Next Array Variation) [Accepted]
Intuition

Let's guess that the minimum window will start at S[i]. 
We can assume that S[i] = T[0]. 
Then, we should find the next occurrence of T[1] in S[i+1:], say at S[j]. 
Then, we should find the next occurrence of T[2] in S[j+1:], and so on.

Finding the next occurrence can be precomputed in linear time 
so that each guess becomes O(T)O(T) work.



Algorithm

We can precompute (for each i and letter), next[i][letter]: 
the index of the first occurrence of letter in S[i:], or -1 if it is not found.

Then, we'll maintain a set of minimum windows for T[:j] as j increases. 
At the end, we'll take the best minimum window.
"""

class Solution(object):
	def minWindow(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: str
		"""
		# Time: O(ST)
		# Space: O(S)
		N = len(S)
		nxt = [None] * N
		last = [-1] * 26
		for i in range(N - 1, -1, -1):
			last[ord(S[i]) - ord('a')] = i
			nxt[i] = tuple(last)
		
		windows = [[i, i] for i, char in enumerate(S) if char == T[0]]
		for j in range(1, len(T)):
			letter_index = ord(T[j]) - ord('a')
			windows = [[root, nxt[i + 1][letter_index]]
					  for root, i in windows
					  if 0 <= i < N - 1 and nxt[i + 1][letter_index] >= 0
					 ]
		if not windows:
			return ""
		i, j = min(windows, key = lambda (i, j): j - i)
		return S[i: j + 1]





