# 138 Copy List with Random Pointer

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# Recursion
# Time: O(n)
# Space: O(n)

class Solution1(object):
    def __init__(self):
        #key, val: oldNode, newNode
        self.visitedHash = {}
        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = RandomListNode(head.label)
        self.visitedHash[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

# Iterative
# Time: O(n)
# Space: O(n)

class Solution2(object):
    def __init__(self):
        #key, val: oldNode, newNode
        self.visitedHash = {}
    
    def getClone(self, node):
        if not node:
            return None
        
        if not node in self.visitedHash:
            self.visitedHash[node] = RandomListNode(node.label)
            
        return self.visitedHash[node]
        
        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        oldNode = head
        newNode = RandomListNode(oldNode.label)
        self.visitedHash[oldNode] = newNode
        
        while oldNode:
            newNode.random = self.getClone(oldNode.random)
            newNode.next = self.getClone(oldNode.next)
            
            oldNode = oldNode.next
            newNode = newNode.next
        
        return self.visitedHash[head]

# Iteration
# Time: O(n)
# Space: O(1)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        # create a new weaved list of original and copied nodes
        curr = head
        while curr:
            # clone node
            newNode = RandomListNode(curr.label)
            
            # insert into original list
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        
        # assign random pointers in those cloned nodes
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # split into old and new linked lists
        currOld = head
        currNew = head.next
        headNew = head.next
        while currOld:
            currOld.next = currOld.next.next
            currNew.next = currNew.next.next if currNew.next else None
            currOld = currOld.next
            currNew = currNew.next
        
        return headNew




