# Merge Two Sorted List
# Leetcode 21

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		head = ListNode(None)
		prev = head
		while l1 and l2:
			if l1.val < l2.val:
				prev.next = l1
				l1 = l1.next
			else:
				prev.next = l2
				l2 = l2.next
			prev = prev.next
		prev.next = l1 if l1 else l2
		return head.next
