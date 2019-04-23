# 129 Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursion
        if not root:
            return 0
        
        self.res = 0
        
        def helper(node, currValue):
            if not node.left and not node.right:
                self.res += currValue
                return
            
            if node.left:
                helper(node.left, currValue * 10 + node.left.val)
            if node.right:
                helper(node.right, currValue * 10 + node.right.val)
            return
        
        helper(root, root.val)
        return self.res



class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # iteration
        if not root:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                res += val
            if node.left:
                stack.append((node.left, val * 10 + node.left.val))
            if node.right:
                stack.append((node.right, val * 10 + node.right.val))
        return res
