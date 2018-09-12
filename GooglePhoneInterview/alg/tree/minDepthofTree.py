#min Depth of tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        # not leaf
        if root.left and not root.right:
            return self.minDepth(root.left)+1
        if not root.left and root.right:
            return self.minDepth(root.right)+1
        
        #if root.left and root.right:
        return 1+min(self.minDepth(root.left), self.minDepth(root.right))

