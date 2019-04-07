# 437 Path Sum iii
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Time: O(n * n) worst
        # Time: O(nlogn) avg
        # Space: (n)
        # corner case
        if not root:
            return 0
        return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def findPath(self, root, sum):
        if not root:
            return 0

        sum -= root.val
        res = 1 if sum == 0 else 0
        return res + self.findPath(root.left, sum) + self.findPath(root.right, sum)



# 112 Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_simple1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # use dfs to go through all path
        # recursive
        # Time: O(n), n is number of nodes
        # Space: O(logn), the recusion call logn times if the tree is balanced
        # else: call n times, therefore the space complexity is O(n)

        # edge case
        if not root:
            return False

        sum -= root.val

        if not root.left and not root.right:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution_simple2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Iteration

        # edge case
        if not root:
            return False

        stack = [(root, sum)]
        while stack:
            node, currSum = stack.pop()
            if not node.left and not node.right and currSum == node.val:
                return True
            if node.left:
                stack.append((node.left, sum - node.val))
            if node.right:
                stack.append((node.right, sum - node.right))
        return False











