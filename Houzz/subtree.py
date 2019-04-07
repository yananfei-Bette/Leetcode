# subtree
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=463311
# leetcode 572

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self. right = None


class Solution1(object):
	def isSubtree(self, s, t):
		if not s and not t:
			return True
		if not s or not t:
			return False
		return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

	def isSame(self, s, t):
		if not s and not t:
			return True
		if not s or not t:
			return False
		return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)


class Solution2(object):
	def isSubtree(self, s, t):
		if not s and not t:
			return True
		if not s or not t:
			return False

		sList = self.preorder(s, True)
		tList = self.preorder(t, True)

		return True if tList in sList else False

	def preorder(self, s, left):
		if not s:
			if left:
				return "lnull"
			else:
				return "rnull"

		return "#" + str(s.val) + " " + self.preorder(s.left, True) + self.preorder(s.right, False) 

