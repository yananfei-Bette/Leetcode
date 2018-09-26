# 279 Serialize and Desetialize BT

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # preorder method
        # time: O(n)
        # DFS
        def helper(node, res):
            if node is None:
                res += 'null,'
            else:
                res += str(node.val) + ','
                res = helper(node.left, res)
                res = helper(node.right, res)
            return res
        
        return helper(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # time: O(n)
        # DFS
        def helper(data_list):
            if data_list[0] == 'null':
                data_list.pop(0)
                return None
            
            root = TreeNode(data_list.pop(0))
            root.left = helper(data_list)
            root.right = helper(data_list)
            return root
            
        data_list = data.split(',')
        root = helper(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))