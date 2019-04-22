#invert tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        # recursive
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        '''
        # non recursive
        if not root:
            return None
        Queue = [root]
        while Queue:
            node = Queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                Queue.append(node.left)
            if node.right:
                Queue.append(node.right)
        return root
