# merge k sorted lists
# leetcode 23
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=465084


class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution1(object):
	def mergeKLists(self, lists):
		# minheap
		# Time: O(nlogk)
		# Space: O(n)
		head = prev = ListNode(None)
		minheap = []

		for l in lists:
			if l:
				heapq.heappush(minheap, (l.val, l))


		while minheap:
			val, l = heapq.heappop(minheap)
			prev.next = ListNode(val)
			prev = prev.next
			l = l.next
			if l:
				heapq.heappush(minheap, (l.val, l))

		return head.next


class Solution2(object):
	def mergeKLists(self, lists):
		# D & C
		# Time: O(nlogk)
		# space: O(1)

		#############################
		def mergeTwoLists(a, b):
			head = prev = ListNode(None)
			while a and b:
				if a.val < b.val:
					prev.next = a
					a = a.next
				else:
					prev.next = b
					b = b.next
				prev = prev.next

			prev.next = a if a else b
			return head.next
		#############################


		totalLen = len(lists)
		interval = 1
		while interval < totalLen:
			for i in range(0, totalLen - interval, interval * 2):
				lists[i] = mergeTwoLists(lists[i], lists[i + interval])
			interval *= 2
		return lists[0] if lists else lists
