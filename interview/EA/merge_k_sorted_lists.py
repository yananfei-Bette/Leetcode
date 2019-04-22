# merge k sorted lists
# external sort

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # minheap
        # time: O(logk * n)
        # space: O(n + k)
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
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # D and C
        # Time: O(nlogk)
        # space: O(1)
        def mergeTwoLists(a, b):
            head = prev = ListNode(None)
            while a and b:
                if a.val < b.val:
                    prev.next = ListNode(a.val)
                    a = a.next
                    prev = prev.next
                else:
                    prev.next = ListNode(b.val)
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
        return lists[0] if lists else lists
        
        