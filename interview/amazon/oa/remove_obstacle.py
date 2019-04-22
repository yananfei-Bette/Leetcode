# remove obstacle
# leetcode 505

class Solution(object):
	def uniquePathsWithObstacles(self, Grid):
		"""
		:type Grid: List[List[int]]
		:rtype: int
		"""
		if not Grid or not Grid[0]:
			return -1
		if Grid[0][0] == 0:
			return -1
		if Grid[0][0] == 9:
			return 0
		
		m = len(Grid)
		n = len(Grid[0])
		dx = [-1, 0, 0, 1]
		dy = [0, 1, -1, 0]

		queue = [(0, 0)]
		
		dist = [[float("inf")] * n for _ in range(m)]
		dist[0][0] = 0

		while queue:
			curr = queue.pop(0)
			# print(curr)
			for i in range(4):
				nextPos = (curr[0] + dx[i], curr[1] + dy[i])
				if 0 <= nextPos[0] < m and 0 <= nextPos[1] < n and Grid[nextPos[0]][nextPos[1]] in {1, 9}:
					if Grid[curr[0]][curr[1]] == 9:
						goal = curr

					if dist[curr[0]][curr[1]] + 1 < dist[nextPos[0]][nextPos[1]]:
						dist[nextPos[0]][nextPos[1]] = dist[curr[0]][curr[1]]  + 1
						queue.append(nextPos)

		res = dist[goal[0]][goal[1]]
		return res if res != float("inf") else -1


if __name__ == "__main__":
	lot1 = [[1, 0, 0], [1, 0, 0], [1, 9, 1]]
	lot = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]]
	sol = Solution()
	print(sol.uniquePathsWithObstacles(lot))