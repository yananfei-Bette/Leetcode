# 450 Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/93296/Recursive-Easy-to-Understand-Java-Solution
"""
Steps:

1. Recursively find the node that has the same value as the key, 
while setting the left/right nodes equal to the returned subtree



2. Once the node is found, have to handle the below 4 cases

- node doesn't have left or right - return null

- node only has left subtree- return the left subtree

- node only has right subtree- return the right subtree

- node has both left and right - find the minimum value in the right subtree, 
set that value to the currently found node, 
then recursively delete the minimum value in the right subtree
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def findMin(node):
            while node.left:
                node = node.left
            return node
        
        # corner case
        if not root:
            return None
        
        # find required node
        if key < root.val:
            # update root.left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # update root.right
            root.right = self.deleteNode(root.right, key)
        else:
            # root.val == key find!
            if not root.left:
                # case 1: leaf
                # case 2: right child only
                return root.right
            elif not root.right:
                # case 3: left child only
                return root.left
            else:
                # case 4: left child and right child
                minNode = findMin(root.right)
                root.val = minNode.val
                # update right
                root.right = self.deleteNode(root.right, root.val)
        return root
            
        




















