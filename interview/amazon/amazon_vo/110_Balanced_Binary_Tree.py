# 110 Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        # edge case
        if not root:
            return True

        if abs(depth(root.left) - depth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
