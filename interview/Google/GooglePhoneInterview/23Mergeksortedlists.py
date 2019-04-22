# 23 Merge k sorted lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        # Brute Force
        # time: O(n*logn)
        # get value, sort it and create another link list
        node = []
        for l in lists:
            while l:
                node.append(l.val)
                l = l.next
        head = point = ListNode(0)
        for v in sorted(node):
            point.next = ListNode(v)
            point = point.next
        return head.next
        '''
        ##############################
        '''
        # use PriorityQueue to save points, or we can use minheap
        # time: O(N*logk)
        # space: O( N + k)
        from Queue import PriorityQueue
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
                
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
        '''
        ''''
        # minheap
        head = point = ListNode(0)
        minheap = []
        for l in lists:
            if l:
                heapq.heappush(minheap, (l.val, l))
        while minheap:
            val, node = heapq.heappop(minheap)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(minheap, (node.val, node))
        return head.next
        '''
        #################################
        # D & C
        # pair k linked lists, for each two lists , we use merge-two method
        # time: O(N*logk)
        # space: O(1)
        def merge2lists(l1, l2):
            head = point = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l2.next
                point = point.next
            point.next = l1 if l1 else l2
            return head.next
        
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in xrange(0, amount - interval, interval * 2):
                lists[i] = merge2lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
    
        