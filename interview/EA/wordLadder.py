# wordLadders
# leetcode 127

class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		# graph with bfs
		wordDic = set(wordList)
		wordDic.discard(beginWord)
		if endWord not in wordDic:
			return 0

		queue = [beginWord]
		level = 1

		while queue:
			nextLevel = []
			for word in queue:
				if word == endWord:
					return level

				for i in range(len(word)):
					for j in range(26):
						temp = list(word)
						temp[i] = chr(ord('a') + j)
						candidate = ''.join(temp)

						if candidate in wordDic:
							nextLevel.append(candidate)
							wordDic.discard(candidate)
			queue = nextLevel
			level += 1

		return 0