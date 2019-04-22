# Maze
# Similar problem: Leetcode 490 The Maze (a little different)
# 1 means obstacle
# 0 means empty

# Intervation, BFS
# Find the destination
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
        
        while queue:
            curr = queue.pop(0)
            if curr == destination:
                return True
            maze[curr[0]][curr[1]] = 1
            
            for i in range(4):
                nextPos = [curr[0] + self.dx[i], curr[1] + self.dy[i]]
                if 0 <= nextPos[0] < m and 0 <= nextPos[1] < n and maze[nextPos[0]][nextPos[1]] == 0:
                    queue.append(nextPos)
        return False

def main():
	maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
	start = [0,4]
	destination = [3,2]
	sol = Solution()
	print(sol.hasPath(maze, start, destination))
	return

if __name__ == "__main__":
	main()



######################################################################
# Leetcode 490
# Keep moving. Ball

class Solution490(object):
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

###################################################################
# Leetcode 505 The Maze II
# Find the shortest path
class Solution505(object):
	def __init__(self):
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, 1, -1, 0]
    
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return -1
        if start == destination:
            return 0
        
        m = len(maze)
        n = len(maze[0])
        queue = [start]
        distance = [[float("inf")] * n for _ in range(m)]
        distance[start[0]][start[1]] = 0
        
        while queue:
            curr = queue.pop(0)
            for i in range(4):
                nextPos = [curr[0] + self.dx[i], curr[1] + self.dy[i]]
                count = 0
                
                while 0 <= nextPos[0] < m and 0 <= nextPos[1] < n and maze[nextPos[0]][nextPos[1]] == 0:
                    count += 1
                    nextPos = [nextPos[0] + self.dx[i], nextPos[1] + self.dy[i]]
                    
                nextPos = [nextPos[0] - self.dx[i], nextPos[1] - self.dy[i]]
                if distance[curr[0]][curr[1]] + count < distance[nextPos[0]][nextPos[1]]:
                    distance[nextPos[0]][nextPos[1]] = distance[curr[0]][curr[1]] + count
                    queue.append(nextPos)
        
        res = distance[destination[0]][destination[1]]
        return res if res != float("inf") else -1


###################################################################
# Leetcode 62 Unique Path
# How many possible unique paths
# DP

class Solution62(object):
	def uniquePaths(self, m, n):
		dp = [[0] * n for _ in range(m)]
		for i in range(m):
			dp[i][0] = 1
		for i in range(n):
			dp[0][i] = 1
		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[-1][-1]

######################################################################
# Leetcode 63
# Contains obstacles

class Solution63(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
			return 0
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
			return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(1, m):
            if not obstacleGrid[i][0]:
                dp[i][0] = (1 - obstacleGrid[i - 1][0]) * dp[i - 1][0]
        for i in range(1, n):
            if not obstacleGrid[0][i]:
                dp[0][i] = (1 - obstacleGrid[0][i - 1]) * dp[0][i - 1]
        
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = (1 - obstacleGrid[i - 1][j]) * dp[i - 1][j] + (1 - obstacleGrid[i][j]) * dp[i][j - 1]
        return dp[-1][-1]	

