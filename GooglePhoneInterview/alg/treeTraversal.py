# tree traversal

# Preorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        #recursive
        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)
        res = []
        helper(root)
        return res
        '''
        #non-recursive
        res = []
        treeStack = []
        node = root
        while node or treeStack:
            if node:
                res.append(node.val)
                treeStack.append(node)
                node = node.left
            else:
                node = treeStack.pop()
                node = node.right
        return res


# Inorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        #recursive
        def helper(node):
            if node:
                helper(node.left)
                res.append(node.val)
                helper(node.right)
        
        res = []
        helper(root)
        return res
        '''
        #non recursive
        res = []
        treeStack = []
        node = root
        while node or treeStack:
            if node:
                treeStack.append(node)
                node = node.left
            else:
                node = treeStack.pop()
                res.append(node.val)
                node = node.right
        return res

# Postorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        # recursive
        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                res.append(node.val)
        
        res = []
        helper(root)
        return res
        '''
        #non recursive
        res = []
        treeNode = []
        node = root
        lastVisited = root
        while node or treeNode:
            #left subtree
            while node:
                treeNode.append(node)
                node = node.left
            node = treeNode[-1]
            #check whether traverse right subtree
            #if yes, print root node
            if not node.right or lastVisited == node.right:
                res.append(node.val)
                treeNode.pop()
                lastVisited = node
                node = None
            # if not, traverse ritht subtree
            else:
                node = node.right
        return res
