# Serialize and Deserialize Binary tree
# leetcode 297

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec1:

	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		def helper(root, res):
			if not root:
				res += "null" + ","
			else:
				res += str(root.val) + ","
				res = helper(root.left, res)
				res = helper(root.right, res)
			return res
		
		res = helper(root, "")
		# print res
		return res
		

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		def helper(data):
			if data[0] == "null":
				data.pop(0)
				return None
			node = TreeNode(data.pop(0))
			node.left = helper(data)
			node.right = helper(data)
			return node
			
		data = data.split(",")
		# print data
		res = helper(data)
		# print data
		return res
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




############################################################
# 449. Serialize and Deserialize BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 297. Serialize and Deserialize Binary Tree
class Codec2:

	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		def tree2str(node):
			if not node:
				return "null"
			return str(node.val) + ',' + tree2str(node.left) + ',' + tree2str(node.right)
		
		if not root:
			return ""
		return tree2str(root)
		

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		def str2tree(data, ind):
			if ind >= len(data) or data[ind] == "null":
				return [None, ind + 1]
			node = TreeNode(data[ind])
			ind += 1
			node.left, ind = str2tree(data, ind)
			node.right, ind = str2tree(data, ind)
			return [node, ind]
			
		if not data:
			return None
		return str2tree(data.split(','), 0)[0]
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))





