# 103 Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # edge case
        if not root:
            return []

        res = [[root.val]]
        queue = [root]
        isLeft = False

        while queue:
            nextLevel = []
            nextLevelVal = []

            for node in queue:
                if node.left:
                    nextLevel.append(node.left)
                    nextLevelVal.append(node.left.val)
                if node.right:
                    nextLevel.append(node.right)
                    nextLevelVal.append(node.right.val)

            queue = nextLevel
            if nextLevelVal:
                if isLeft:
                    res.append(nextLevelVal)
                else:
                    res.append(nextLevelVal[::-1])
                isLeft = not isLeft

        return res
