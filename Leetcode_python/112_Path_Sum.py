# 112 Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# use dfs to go through all path
# Time: O(n), n is number of nodes
# Space: O(logn), the recusion call logn times if the tree is balanced
# else: call n times, therefore the space complexity is O(n)


# Recursion
class Solution1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)



class Solution2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """        
        # Iteration
        if not root:
            return False

        stack = [(root, sum)]
        while stack:
            node, sum = stack.pop()

            if not node.left and not node.right and node.val == sum:
                return True

            if node.left:
                stack.append((node.left, sum - node.val))
            if node.right:
                stack.append((node.right, sum - node.val))
        
        return False
        
