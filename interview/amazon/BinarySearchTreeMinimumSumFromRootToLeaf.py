# Binary search tree minimum sum from root to leaf
# recursion

class Solution(object):
	def minSum(self, root):
		if not root:
			return 0
		if root.left and not root.right:
			return self.minSum(root.left) + root.val
		if not root.left and root.right:
			return self.minSum(root.right) + root.val
		return min(self.minSum(root.left), self.minSum(root.right)) + root.val