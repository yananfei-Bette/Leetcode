# Number of Island
# leetcode 200

class Solution1(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		# dfs

		seen = set()
		
		#######
		def dfs(r, c):
			if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c] == '1'):
				return 0
			seen.add((r, c))
			return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
		########
		
		return len([1 for i in range(len(grid)) for j in range(len(grid[0])) if dfs(i, j) != 0])



class Solution2(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		# recursion

		##########
		def dfs(r, c):
			if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1'):
				return
			grid[r][c] = '0'
			dfs(r - 1, c)
			dfs(r + 1, c)
			dfs(r, c - 1)
			dfs(r, c + 1)
			return
		##########
		
		if not grid or not grid[0]:
			return 0
		numIsland = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					numIsland += 1
					dfs(i, j)
		return numIsland



class Solution3(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		# iteration
		if not grid or not grid[0]:
			return 0
		numIsland = 0
		dirr = [-1, 1, 0, 0]
		dirc = [0, 0, -1, 1]
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					numIsland += 1
					grid[i][j] = '0'
					queue = [(i, j)]
					while queue:
						r, c  = queue.pop(0)
						for dr, dc in zip(dirr, dirc):
							cr, cc = r + dr, c + dc
							if 0 <= cr < len(grid) and 0 <= cc < len(grid[0]) and grid[cr][cc] == '1':
								queue.append((cr, cc))
								grid[cr][cc] = '0'
		return numIsland
		