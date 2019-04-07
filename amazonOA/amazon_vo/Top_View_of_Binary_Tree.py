# Top View of Binary Tree

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# change form
# 98 Valid Binary Search tree
class Solution1(object):
    def TopView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [(0, 0, 0, root)]
        res = [root.val]
        while queue:
            col, minVal, maxVal, node = queue.pop(0)
            if col < minVal:
                res.append(node.val)
            elif col > maxVal:
                res.append(node.val)

            if node.left:
                queue.append((col - 1, min(minVal, col), maxVal, node.left))
            if node.right:
                queue.append((col + 1, minVal, max(col, maxVal), node.right))

        return res


# change form
# 314 Binary Trree Vertical Order Traversal
class Solution2(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[]
        """
        if not root:
            return []

        queue = [(0, root)]
        hashset = {0}
        res = [root.val]

        while queue:
            col, node = queue.pop(0)
            if node.left:
                queue.append((col - 1, node.left))
                if col - 1 not in hashset:
                    hashset.add(col - 1)
                    res.append(node.left.val)
            if node.right:
                queue.append((col + 1, node.right))
                if col + 1 not in hashset:
                    hashset.add(col + 1)
                    res.append(node.right.val)

        return res


# review code
# 98 Valid Binary search tree

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion
class Solution_98_1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # edge case
        if not root:
            return True

        def inorderTraversal(node, minVal, maxVal):
            if minVal != None and node.val <= minVal:
                return False
            if maxVal != None and node.val >= maxVal:
                return False

            left, right = True, True
            if node.left:
                left = inorderTraversal(node.left, minVal, node.val)
            if node.right:
                right = inorderTraversal(node.right, node.val, maxVal)
            return left and right

        return inorderTraversal(root, None, None)

# Interation
class Solution_98_1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, None, None)]
        while stack:
            node, minVal, maxVal = stack.pop()
            if minVal != None and node.val <= minVal:
                return False
            if maxVal != None and node.val >= maxVal:
                return False

            if node.left:
                stack.append((node.left, minVal, node.val))
            if node.right:
                stack.append((node.right, node.val, maxVal))

        return True



# 314 Binary Tree Vertical Order Traversal

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # edge case
        if not root:
            return []

        queue = [(0, root)]
        hashtable = {0: [root.val]}

        while queue:
            col, node = queue.pop(0)
            if node.left:
                queue.append((col - 1, node.left))
                hashtable[col - 1] = hashtable.get(col - 1, []) + [node.left.val]
            if node.right:
                queue.append((col + 1, node.right))
                hashtable[col + 1] = hashtable.get(col + 1, []) + [node.right.val]

        res = []
        for key, val in sorted(hashtable.items()):
            res.append(val)

        return res

