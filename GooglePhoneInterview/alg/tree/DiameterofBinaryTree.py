#Diameter of Binary tree
# maxDepth

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(node):
            if not node:
                return 0
            l = maxDepth(node.left)
            r = maxDepth(node.right)
            self.diameter = max(self.diameter, l+r)
            return 1+max(l, r)
        maxDepth(root)
        return self.diameter
        

