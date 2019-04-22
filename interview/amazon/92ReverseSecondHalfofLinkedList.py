# Reverse Second Half of Linked List
# Leetcode 92

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# recursion
# Time: O(n)
# Spacw: O(n)
class Solution1(object):
	def __init__(self):
		self.left = None
		self.stop = False

	def reverseBetween(self, head, m, n):
		if not head:
			return head
		self.recurse(right, m, n)
		return head

	def recurse(right, m, n):
		if n == 1:
			return

		right = right.next

		if m > 1:
			self.left = self.left.next

		self.recurse(right, m - 1, n - 1)

		if self.left == right or self.left = right.next:
			self.stop = True

		if not self.stop:
			self.left.val, right.val = right.val, self.left.val
		return

# Interative Link Reversal
# Time: O(n)
# Space: O(1)

class Solution2(object):
	def reverseBetween(self, head, m, n):
		if not head:
			return head

		prev, curr = None, head
		while m > 1:
			prev = curr
			curr = curr.next
			m -= 1
			n -= 1

		con, tail = prev, curr
		while n:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
			n -= 1

		if con:
			con.next = prev
		else:
			head = prev
		tail.next = curr
		return head

# Reverse Second half
class Solution3(object):
	def reverseSecondHalf(self, head):
		if not head:
			return head

		slow, fast = head, head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next

		prev = None
		curr = slow.next

		while curr:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode

		slow.next = prev

		return head
