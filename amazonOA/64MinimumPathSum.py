# Minimum Path Sum
# Leetcode 64
# Similar to Unique Path
# DP

class Solution64(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


##############################################
# Leetcode 113
# Tree
# DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution113(object):
    def __init__(self):
        self.res = []
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return self.res
        self.dfs(root, sum, [])
        return self.res
    
    def dfs(self, node, remain, currList):
        if not node:
            return
        if not node.left and not node.right and node.val == remain:
            self.res.append(currList + [node.val])
            return
        if node.left:
            self.dfs(node.left, remain - node.val, currList + [node.val])
        if node.right:
            self.dfs(node.right, remain - node.val, currList + [node.val])
        return

###########################################
# Minimum Path Sum
# Reference: from little potaknife

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def minPathSum(root):
		if not root:
			return 0
		if root.left and not root.right:
			return self.minPath(root.left) + root.val
		if not root.left and root.right:
			return self.minPathSum(root.right) + root.val
		return min(self.minPathSum(root.left), self.minPathSum(root.right)) + root.val

