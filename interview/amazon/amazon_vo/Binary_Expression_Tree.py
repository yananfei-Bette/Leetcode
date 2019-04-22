# Binary Expression Tree
class Solution(object):
    def BinaryExpressionTree(self, root):
        """
        :type prices: TreeNode
        :rtype: str
        """
        def hepler(node):
            if not node.left and not node.right:
                return str(node.val)
            return "(" + helper(root.left) + str(root.val) + helper(root.right) + ")"

        if not root:
            return ""
        res = helper(root)
        return res
