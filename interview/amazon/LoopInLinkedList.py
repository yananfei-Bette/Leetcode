# Loop in Linked List
# Find if there is any loop in a linked list. If yes, where is the beginning

class ListNode(object):
	def __init__(self, v):
		self.val = v
		self.next = None

class Solution(objcet):
	def hasCycle(self, head):
		if not head:
			return False
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
			return False

	def detectCycle(self, head):
		if not head or not head.next:
			return None
		slow = head
		fast = head
		entry = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				while entry != slow:
					entry = entry.next
					slow = slow.next