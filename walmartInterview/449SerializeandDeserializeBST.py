#449 Serialize and Deserialize BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def tree2str(node):
            if not node:
                return 'null'
            return str(node.val)+','+tree2str(node.left)+','+tree2str(node.right)
        if not root:
            return ''
        return tree2str(root)
        
        

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def str2tree(s,ind):
            if ind >= len(s) or s[ind] == 'null':
                return [None, ind+1]
            node = TreeNode(s[ind])
            node.left, ind = str2tree(s,ind+1)
            node.right, ind = str2tree(s, ind)
            return [node, ind]
        if not data:
            return None
        return str2tree(data.split(','),0)[0]
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))