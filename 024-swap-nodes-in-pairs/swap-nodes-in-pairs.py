# -*- coding:utf-8 -*-


#
# Given a linked list, swap every two adjacent nodes and return its head.
#
#
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        
        fakehead = ListNode(0)
        fakehead.next = head
        
        # l1--> 1--> 2--> 3--> 4
        #       l2
        l1 = fakehead
        l2 = head
        while l2 and l2.next:
            _next = l2.next.next
            l1.next = l2.next
            l2.next.next = l2
            l2.next = _next
            l1 = l2
            l2 = _next
        
        return fakehead.next
            
