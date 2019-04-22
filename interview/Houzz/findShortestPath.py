# find shortest path
# like amazon remove obstacle
# leetcode 505 maze II
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=456875

# find path
class Solution(object):
	def __init__(self):
		self.dx = [-1, 0, 0 ,1]
		self.dy = [0, 1, -1, 0]
		
	def hasPath(self, maze, start, destination):
		"""
		:type maze: List[List[int]]
		:type start: List[int]
		:type destination: List[int]
		:rtype: bool
		"""
		if not maze or not maze[0]:
			return False
		if maze[start[0]][start[1]] == 1:
			return False
		if maze[destination[0]][destination[1]] == 1:
			return False
		if start == destination:
			return True
		
		m = len(maze)
		n = len(maze[0])
		queue = [start]
		visited = [[False] * n for _ in range(m)]
		visited[start[0]][start[1]] = True
		
		while queue:
			curr = queue.pop(0)
			if curr == destination:
				return True
			
			for i in range(4):
				nextPos = [curr[0] + self.dx[i], curr[1] + self.dy[i]]
				while 0 <= nextPos[0] < m and 0 <= nextPos[1] < n and maze[nextPos[0]][nextPos[1]] == 0:
					nextPos = [nextPos[0] + self.dx[i], nextPos[1] + self.dy[i]]
				if not visited[nextPos[0] - self.dx[i]][nextPos[1] - self.dy[i]]:
					queue.append([nextPos[0] - self.dx[i], nextPos[1] - self.dy[i]])
					visited[nextPos[0] - self.dx[i]][nextPos[1] - self.dy[i]] = True
		return False


# find shortest path
class Solution2(object):
	def uniquePathWithObstacles(self, Grid):
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
			if Grid[curr[0]][curr[1]] == 9:
				goal = curr

			for i in range(4):
				nextPos = (curr[0] + dx[i], curr[1] + dy[i])
				if 0 <= nextPos[0] < m and 0 <= nextPos[1] < n and Grid[nextPos[0]][nextPos[1]] in {1, 9}:
					if dist[curr[0]][curr[1]] + 1 < dist[nextPos[0]][nextPos[1]]:
						dist[nextPos[0]][nextPos[1]] = dist[curr[0]][curr[1]] + 1
						queue.append(nextPos)

		res = dist[goal[0]][goal[1]]
		return res if res != float("inf") else -1


# print path
# leetcode 499 maze III
# https://leetcode.com/problems/the-maze-iii/discuss/150550/Python-Short-PriorityQueue-solution-beats-100
class Solution3(object):
	def findShortestWay(self, maze, ball, hole):
		if not maze or not maze[0]:
			return "impossible"
		if maze[ball[0]][ball[1]] == 1 or maze[hole[0]][hole[1]] == 1:
			return "impossible"
		if ball == hole:
			return ""

		m = len(maze)
		n = len(maze[0])

		minheap = [(dist, pattern, ball[0], ball[1])]
		visited = {(ball[0], ball[1]): [0, ""]}

		while minheap:
			dist, pattern, x, y = heapq.heappop(minheap)
			if [x, y] == hole:
				return pattern

			for dx, dy, action in [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]:
				nextX, nextY, count = x, y, 0
				while 0 <= nextX + dx < m and 0 <= nextY + dy < n and maze[nextX + dx][nextY + dy] == 0:
					nextX += dx
					nextY += dy
					count += 1
					if [nextX, nextY] == hole:
						break

				if (nextX, nextY) not in visited or [dist + count, pattern + action] < visited[(nextX, nextY)]:
					visited[(nextX, nextY)] = [dist + count, pattern + action]
					heapq.heappush((dist + count, pattern + action, nextX, nextY))
		return "impossible"


