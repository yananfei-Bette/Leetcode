# subtree
# leetcode 572 subtree of another tree

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# recursion
# Time: O(m * n)
# Spce: O(n)
class Solution1(object):
	def isSubTree(self, T1, T2):
		if not T2:
			return True
		if not T1:
			return False
		return self.isSame(T1, T2) or self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

	def isSame(self, T1, T2):
		if not T1 and not T2:
			return True
		if not T1 or not T2:
			return False
		if T1.val != T2.val:
			return False
		return self.isSame(T1.left, T2.left) and self.isSame(T1.right, T2.right)

# Using preorder traversal
# Time: O(m^2 + n^2 + m*n)
# Space: O(max(m, n))
class Solution2(object):
	def isSubtree(self, s, t):
		tree1 = self.preorder(s, True)
		tree2 = self.preorder(t, True)
	return True if tree2 in tree1 else False

	def preorder(self, node, leftSubtree):
		if not node:
			if leftSubtree:
				return "lnull"
			else:
				return "rnull"
		return "#" + str(node.val) + " " + self.preorder(node.left, True) + self.preorder(node.right, False)
