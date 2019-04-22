# 21 Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Iteration
        # Time: O(m + n)
        # Space: O(1)

        # edge case
        if not (l1 and l2):
            return l1 if l1 else l2

        head = prev = ListNode(None)
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


class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Recursion
        # Time: O(m + n)
        # Space: O(m + n)

        # edge case
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# follow up
# 23 Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# minheap
# Time: O(nlogk)
# Space: O(n)
class Solution_followUp1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # edge case:
        if not lists:
            return None

        head = prev = ListNode(None)
        minheap = []

        # initialize minheap
        for l in lists:
            if l:
                heapq.heappush(minheap, (l.val, l))

        # link
        while minheap:
            val, l = heapq.heappop(minheap)
            prev.next = ListNode(val)
            prev = prev.next
            l = l.next
            if l:
                heapq.heappush(minheap, (l.val, l))

        return head.next


# D & C
# Time: O(nlogk)
# Space: O(1)
class Solution_followUp2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # edge case
        if not lists:
            return None

        def mergeTwoLists(a, b):
            # edge case
            if not a:
                return b
            if not b:
                return a

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

        totalLen = len(lists)
        interval = 1
        while interval < totalLen:
            for i in range(0, totalLen - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]



