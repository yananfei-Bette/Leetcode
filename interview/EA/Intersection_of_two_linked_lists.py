# Intersection of two linked lists
# leetcode 160

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		hashset = set()
		currA = headA
		while currA:
			hashset.add(currA)
			currA = currA.next
		
		currB = headB
		while currB:
			if currB in hashset:
				return currB
			currB = currB.next
		return None


class Solution2(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		# two pointers
		if not headA or not headB:
			return None
		
		pA = headA
		pB = headB
		while pA != pB and(pA or pB):
			if not pA:
				pA = headB
			if not pB:
				pB = headA
			if pA == pB:
				break
			
			pA = pA.next
			pB = pB.next
		return pA if pA == pB else None
		