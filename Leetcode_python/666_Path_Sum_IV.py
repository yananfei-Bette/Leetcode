# 666 Path Sum IV

# construct tree and traversal the tree
# Time: O(n)
# Space: O(n)
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution1(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = Node(nums[0] % 10)
        
        for num in nums[1:]:
            depth, pos, val = num / 100, num / 10 % 10, num % 10
            pos -= 1
            curr = root
            for d in range(depth - 2, -1, -1):
                if pos < 2 ** d:
                    if not curr.left:
                        curr.left = Node(val)
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = Node(val)
                    curr = curr.right
                pos %= 2 ** d
        
        self.res = 0
        
        def dfs(node, currSum = 0):
            if not node:
                return
            
            currSum += node.val
            if not node.left and not node.right:
                self.res += currSum
            else:
                dfs(node.left, currSum)
                dfs(node.right, currSum)
            return
        
        dfs(root)
        return self.res



# Inspired by approach 1
# Use dic to represent position: val pair
# Because it is a full binary tree
# parent node: 10 * depth + pos
# left child: 10 * (depth + 1) + 2 * pos - 1
# right child: 10 * (depth + 1) + 2 * pos

# Time: O(n)
# Space: O(n)
class Solution2(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        self.res = 0
        # 10 * depth + pos: val
        values = {num / 10: num % 10 for num in nums}
        
        def dfs(node, currSum = 0):
            if node not in values:
                return
            
            currSum += values[node]
            depth, pos = node / 10, node % 10
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1
            
            if left not in values and right not in values:
                self.res += currSum
            else:
                dfs(left, currSum)
                dfs(right, currSum)
            return
        
        dfs(nums[0] / 10)
        return self.res
        

