# LCA of Deepest Nodes in binary tree
# https://www.cnblogs.com/EdwardLiu/p/6551606.html
# https://github.com/interviewdiscussion/files/blob/master/Facebook%E9%A2%98%E8%A7%A3/Lowest%20Common%20Ancestor%20of%20Deepest%20Nodes%20in%20a%20Tree.java
# https://www.1point3acres.com/bbs/thread-148413-1-1.html

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.maxDepth = 0
		self.children = []


# Recursion
# Time: O(n), n is the number of nodes
# Space: 
class Solution1(object):
	def lowestCommonAncestor(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# post order traversal, use recursion
		# if not root or root is leaf, return None
		if not root or not root.children:
			return None

		# curr tree's deepest leaf depth
		currMaxDepth = 0
		# num of deepest leaves
		countMaxDepth = 0

		nodeLCA = TreeNode(None)

		for child in root.children:
			temp = self.lowestCommonAncestor(child)
			if not temp:
				continue
			elif temp.maxDepth > currMaxDepth:
				currMaxDepth = temp.maxDepth
				nodeLCA = temp
				countMaxDepth = 1
			elif temp.maxDepth == currMaxDepth:
				countMaxDepth += 1

		if countMaxDepth > 1:
			root.maxDepth = nodeLCA.maxDepth + 1
			return root
		elif countMaxDepth == 1:
			nodeLCA.maxDepth += 1
			return nodeLCA
		elif countMaxDepth == 0:
			root.maxDepth = 2
			return root


# Iteration
class Solution2(object):
	def lowestCommonAncestor(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# use post orderr traversal, iteration
		if not root or not root.children:
			return None

		stack = [root]
		while stack:
			



