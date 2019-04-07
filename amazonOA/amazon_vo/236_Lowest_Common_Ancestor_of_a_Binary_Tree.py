# 236 Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
# Time: O(n)
# Space: O(n)
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(currNode):
            if not currNode:
                return False

            left = helper(currNode.left)
            right = helper(currNode.right)

            mid = currNode == p or currNode == q

            if mid + left + right >= 2:
                self.ans = currNode

            return mid or left or right

        # corner case
        if not root:
            return None

        # dfs
        self.ans = None
        helper(root)

        return self.ans

# recursion
#################
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right,p ,q)

        if l and r:
            return root
        if l:
            return l
        if r:
            return r
        return None


# Iterative using parent pointers
###################
'''
If we have parent pointers for each node, 
we can traverse back from p and q to get their ancestors. 
The first common node we get during this traversal would be the LCA node.

We can save the parent pointers in a dictionary as we traverse the tree.
'''
# Time: O(n)
# Space: O(n)
class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestorsP = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q


# Iterative withour parent pointers
class Solution4(object):

    # Three static flags to keep track of post-order traversal.

    def __init__(self):
        # Both left and right traversal pending for a node.
        # Indicates the nodes children are yet to be traversed.
        self.BOTH_PENDING = 2

        # Left traversal done.
        self.LEFT_DONE = 1

        # Both left and right traversal done for a node.
        # Indicates the node can be popped off the stack.
        self.BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # corner case
        if not root:
            return None


        stack = [(root, self.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1

        while stack:
            parentNode, parentState = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parentState != self.BOTH_DONE:

                # If both child traversals are pending
                if parentState == self.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parentNode == p or parentNode == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    childNode = parentNode.left
                else:
                    # traverse right child
                    childNode = parentNode.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parentNode, parentState - 1))

                # Add the child node to the stack for traversal.
                if childNode:
                    stack.append((childNode, self.BOTH_PENDING))

            else:
                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack.
                # Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None



# 235 Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Lets review properties of a BST:

1. Left subtree of a node N contains nodes 
whose values are lesser than or equal to node N's value.

2. Right subtree of a node N contains nodes 
whose values are greater than node N's value.

3. Both left and right subtrees are also BSTs.
'''

# Recursion
# Time: O(n)
# Space: O(1)
class Solution_simple1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# Iteration
# Time: O(n)
# Space: O(1)
class Solution_simple2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > max(p.val, q.val):
                if node.left:
                    stack.append(node.left)
            elif node.val < min(p.val, q.val):
                if node.right:
                    stack.append(node.right)
            else:
                return node

