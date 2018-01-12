# -*- coding:utf-8 -*-


#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre = head
        while pre:
            if pre.next and pre.next.val == pre.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        
        return head
        
