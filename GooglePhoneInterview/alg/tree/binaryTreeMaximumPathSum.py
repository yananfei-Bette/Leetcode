# binary tree maximum path sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxPathSumVal = float('-inf')
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(node):
            if not node:
                return 0
            currentVal = node.val
            l = maxDepth(node.left)
            r = maxDepth(node.right)
            if l > 0:
                currentVal += l
            if r > 0:
                currentVal += r
            self.maxPathSumVal = max(self.maxPathSumVal, currentVal)
            return max(node.val, node.val+max(l,r))
        
        maxDepth(root)
        return self.maxPathSumVal
        
