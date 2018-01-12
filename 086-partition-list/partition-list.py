# -*- coding:utf-8 -*-


# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        ge_head = ListNode(0)
        l_head = ListNode(0)
        ge = ge_head; l = l_head
        p = head
        while p:
            if p.val >= x:
                ge.next = p
                ge = ge.next
            else:
                l.next = p
                l = l.next
            p = p.next
        
        ge.next = None
        l.next = ge_head.next
        return l_head.next
        
