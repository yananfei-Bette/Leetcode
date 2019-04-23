# 687 Longest Univalue Path

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def __init__(self):
        self.res = 0
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        curr = 0
        l, r = 0, 0
        if root.left and root.left.val == root.val:
            l = self.helper(root.left) + 1
        if root.right and root.right.val == root.val:
            r = self.helper(root.right) + 1
        
        if l > 0:
            curr += l
        if r > 0:
            curr += r
        
        self.res = max(self.res, curr)
        
        self.longestUnivaluePath(root.left)
        self.longestUnivaluePath(root.right)
        
        return self.res
    
    
    def helper(self, root):
        if not root:
            return 0
        
        l, r = 0, 0
        if root.left and root.left.val == root.val:
            l = self.helper(root.left) + 1
        if root.right and root.right.val == root.val:
            r = self.helper(root.right) + 1
        
        return max(l, r)



class Solution2(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(logn)
        self.res = 0
        
        def helper(node):
            if not node:
                return 0
            
            l = helper(node.left)
            r = helper(node.right)
            
            left, right = 0, 0
            if node.left and node.left.val == node.val:
                left = l + 1
            if node.right and node.right.val == node.val:
                right = r + 1
            
            self.res = max(self.res, left + right)
            return max(left, right)
        
        helper(root)
        return self.res
        
        
