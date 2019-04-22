# Insert into cycle linked list

class ListNode(object):
	def __init__(self, v):
		self.val = v
		self.next = None

class Solution(object):
	def insert(self, head, val):
		if not head:
			res = ListNode(val)
			res.next = res
			return res

		curr = head
		while True:
			if val <= curr.next