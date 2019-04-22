# leetcode 79
# word Search
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=465084

class Solution1(object):
	def exist(self, board, word):
		"""
		:type: board: List[List[str]]
		:type: word: str
		:rtype: bool
		"""
		###########################
		def backtrack(r, c, ind):
			if ind == N:
				return True

			if 0 <= r < R and 0 <= c < C and not visited[r][c] and board[r][c] == word[ind]:
				visited[r][c] = True
				res True and (backtrack(r - 1, c, ind + 1) or
								backtrack(r + 1, c, ind + 1) or
								backtrack(r, c - 1, ind + 1) or
								backtrack(r, c + 1, ind + 1))
				visited[r][c] = False
				return res
			return False
		###########################

		if not board or not board[0]:
			return False
		if not word or len(word) > len(board) * len(board[0]):
			return False

		R = len(board)
		C = len(board[0])
		N = len(word)
		visited = [[False] * C for _ in range(R)]

		res = False
		for r in range(R):
			for c in range(C):
				if board[r][c] == word[0]:
					res |= backtrack(r, c, 0)

		return res




# leetcode 212
# word search II

class Solution2_1(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		# backtrack for each word
		# TLE
		
		#############################
		def backtrack(r, c, ind, word):
			if ind == len(word):
				return True
			
			if 0 <= r < R and 0 <= c < C and board[r][c] == word[ind]:
				char = board[r][c]
				board[r][c] = "*"
				if (backtrack(r - 1, c, ind + 1, word) or
				   backtrack(r + 1, c, ind + 1, word) or
				   backtrack(r, c - 1, ind + 1, word) or
				   backtrack(r, c + 1, ind + 1, word)):
					board[r][c] = char
					return True
				board[r][c] = char
				return False
		#############################
		
		if not board or not board[0]:
			return []
		if not words:
			return []
		
		R = len(board)
		C = len(board[0])
		res = []
		
		for word in words:
			if not word or len(word) > R * C:
				continue
			if word in res:
				continue
			
			for i in range(R):
				for j in range(C):
					if word not in res and board[i][j] == word[0] and backtrack(i, j, 0, word):
						res.append(word)
		return res



class TrieNode():
	def __init__(self):
		self.next = [None] * 26
		self.word = None


class Solution2_2(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		# Trie
		# First build trie tree
		# Find word according to the tree

		if not board or not board[0]:
			return []
		if not words:
			return []

		res = []
		root = self.buildTrie(words)

		for i in range(len(board)):
			for j in range(len(board[0])):
				self.dfs(board, i, j, root, res)
		return res

	def buildTrie(self, words):
		root = TrieNode()

		for word in words:
			node = root

			for char in word:
				ind = ord(char) - ord('a')
				if not node.next[ind]:
					node.next[ind] = TrieNode()
				node = node.next[ind]
			node.word = word
		return root

	def dfs(self, board, r, c, node, res):
		if 0 <= r < len(board) and 0 <= c < len(board[0]):
			char = board[r][c]
			if char == "*" or not node.next[ord(char) - ord('a')]:
				rerturn

			node = node.next[ord(char) - ord('a')]
			if node.word:
				res.append(node.word)
				node.word = None

			board[r][c] = "*"
			self.dfs(board, r - 1, c, node, res)
			self.dfs(board, r + 1, c, node, res)
			self.dfs(board, r, c - 1, node, res)
			self.dfs(board, r, c + 1, node, res)
			board[r][c] = char

		return


