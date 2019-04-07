# merge two sorted lists
#
# this question is kinds of like external sort
# https://stackoverflow.com/questions/20802396/how-external-merge-sort-algorithm-works
# http://faculty.simpson.edu/lydia.sinapova/www/cmsc250/LN250_Weiss/L17-ExternalSortEX1.htm
# http://faculty.simpson.edu/lydia.sinapova/www/cmsc250/LN250_Weiss/L17-ExternalSortEX2.htm

# leetcode 21 merge two sorted lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = prev = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                prev.next = l2
                prev = prev.next
                l2 = l2.next
        prev.next = l1 if l1 else l2
        return head.next