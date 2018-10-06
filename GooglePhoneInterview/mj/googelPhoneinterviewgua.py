# googel Phone interview gua
'''
Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

You are given a binary tree of N nodes. While it's mostly OK, there is one extra edge that violates the tree property. One such example:

    1
   / \
  2   3
 / \ /
4   5
none none

Your job is to find the extra edge and remove it.
'''

#time: O(n)
#space:O(n)
seen = set(root)
def traversal(root):
	if not root:
		return 
	if root.left in seen:
		root.left = None
		return
	else:
		seen.add(root.left)
		traversal(root.left)

	if root.right in seen:
		root.right = None
		return
	else:
		seen.add(root.right)
		traversal(root.right)
	return
	
# for graph BFS
seen = set(root)
def traversal(root):
	queue = [root]
	while queue:
		node = queue.pop(0)
		if node.left and node.left in seen:
			node.left = None
		elif node.left:
			seen.add(node.left)
			queue.append(node.left)
		if node.right and node.right in seen:
			node.right = None
		elif node.right:
			seen.add(node.right)
			queue.append(node.right)
return
			

