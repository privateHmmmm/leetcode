# -*- coding:utf-8 -*-


# Given a linked list, remove the nth node from the end of list and return its head.
#
#
# For example,
#
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        fakehead = ListNode(0)
        fakehead.next = head
        slow = fakehead
        fast = head
        lens = 1

        while fast and fast.next != None:
            fast = fast.next
            if lens >= n:
                slow = slow.next
            else:
                lens += 1

        slow.next = slow.next.next
        return fakehead.next
