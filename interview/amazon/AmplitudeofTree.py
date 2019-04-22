# Amplitude of Tree
# Given a tree of N nodes, return the amplitude of the tree
# The amplitude of path P is the maximum difference among values of nodes on path P. The amplitude of tree T is the maximum amplitude of all paths in T. 

# class TreeNode(object):
# 	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution(object):
	def AmplitudeOfTree(self, root):
		if not root:
			return 0
		return self.helper(root, root.val, root.val)

	def helper(self, node, minVal, maxVal):
		if not node:
			return maxVal - minVal
		if node.val < minVal:
			minVal = node.val
		if node.val > maxVal:
			maxVal = node.val
		return max(self.helper(node.left, minVal, maxVal), 
			self.helper(node.right, minVal, maxVal))

