# -*- coding:utf-8 -*-


# Given a list, rotate the list to the right by k places, where k is non-negative.
#
#
#
# Example:
#
# Given 1->2->3->4->5->NULL and k = 2,
#
# return 4->5->1->2->3->NULL.
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        
        len = 1
        cur = head
        while cur.next:
            len +=1
            cur = cur.next
        
        cur.next = head
        cur = head
        index = 1
        end_index = len - k if len > k else len - k%len  # !!!
        while index < end_index:
            cur = cur.next
            index +=1
        head = cur.next 
        cur.next = None
        return head
            
