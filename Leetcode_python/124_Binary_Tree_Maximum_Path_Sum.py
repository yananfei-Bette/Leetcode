# 124 Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxPathSumVal = float("-inf")
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(logn)
        if not root:
            return 0
        
        def helper(node):
            if not node:
                return 0
            
            currVal = node.val
            
            l = helper(node.left)
            r = helper(node.right)
            
            if l > 0:
                currVal += l
            if r > 0:
                currVal += r
            self.maxPathSumVal = max(self.maxPathSumVal, currVal)
            
            return max(node.val, node.val + max(r, l))
        
        helper(root)
        return self.maxPathSumVal
        