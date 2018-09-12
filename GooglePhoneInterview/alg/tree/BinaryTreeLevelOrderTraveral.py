# binary tree level order traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #BFS
        res = []
        if not root:
            return res
        queue = [root]
        res.append([root.val])
        while queue:
            nextlevel = []
            nextlevelVal = []
            for node in queue:
                if node.left:
                    nextlevel.append(node.left)
                    nextlevelVal.append(node.left.val)
                if node.right:
                    nextlevel.append(node.right)
                    nextlevelVal.append(node.right.val)
            if nextlevelVal:
                res.append(nextlevelVal)
            queue = nextlevel
        return res
