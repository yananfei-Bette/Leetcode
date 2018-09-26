# 876 Middle of the Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        mid, last = head, head
        count = 1
        while last:
            if count % 2 == 0:
                mid = mid.next
            last = last.next
            count += 1
        return mid 
        '''
        # fast and slow pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow