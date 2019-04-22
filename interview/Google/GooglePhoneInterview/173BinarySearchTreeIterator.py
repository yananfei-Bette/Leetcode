# 173 Binary Search Tree Iterator

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative -> stack
# Inorder

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curr = root
        self.stack = []
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # time: O(1)
        if self.stack or self.curr != None:
            return True
        return False
        

    def next(self):
        """
        :rtype: int
        """
        # time: O(1)
        # space: O(h)
        while self.curr != None:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        self.curr = self.stack.pop()
        value = self.curr.val
        self.curr = self.curr.right
        
        return value
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())