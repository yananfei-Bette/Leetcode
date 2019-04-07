# Maximum average subtree
# Lintcode 597
# https://yeqiuquan.blogspot.com/2017/03/lintcode-597-subtree-with-maximum.html


# binary tree

class Solution_binaryTree(object):

	'''
	class ResultType(object):
		def __init__(self, node, sumVal, size):
			self.node = node
			self.sumVal = sumVal
			self.size = size
	'''
	def __init__(self):
		self.result = (None, None, None)


	def findSubtree(self, root):
		if not root:
			return None

		rootResult = self.helper(root)
		return self.result[0]

	def helper(self, root):
		if not root:
			return (None, 0, 0)

		leftResult = self.helper(root.left)
		rightResult = self.helper(root.right)

		currResult = (root, leftResult[1] + rightResult[1] + root.val, leftResult[2] + rightResult[2] + 1)

		if self.result[0] == None or currResult[1] * self.result[2] > self.result[1] * currResult[2]:
			self.result = currResult

		return currResult


# multiple subtrees
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=478916
class Solution_multipleSubtrees(object):
	def __init__(self):
		self.res = (None, None, None)

	def findSubtree(self, root):
		if not root:
			return None

		rootResult = self.helper(root)
		return self.result[0]

	def helper(self, root):
		if not root:
			return (None, 0, 0)

		res = []
		for child in root.children:
			res.append(self.helper(child))

		currSum = 0
		currSize = 0
		for r in res:
			currSum += r[1]
			currSize += r[2]

		currResult = (root, currSum + root.val, currSize + 1)
		if self.result[0] == None or currResult[1] * self.result[2] > self.result[1] * currResult[2]:
			if currResult[2] > 1:
				self.result = currResult

		return currResult


















