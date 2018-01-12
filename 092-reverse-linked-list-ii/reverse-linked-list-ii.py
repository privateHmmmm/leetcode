# -*- coding:utf-8 -*-


#
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
#
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
#
# return 1->4->3->2->5->NULL.
#
#
# Note:
# Given m, n satisfy the following condition:
# 1 &le; m &le; n &le; length of list.
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        fakehead = ListNode(0)
        fakehead.next = head
        
        node = fakehead
        k = 1
        while node and k<m:
            node=node.next
            k +=1
        
        if not node or not node.next: return head
        
        pre = node
        cur = node.next
        
        while cur and k<n:
            # head insert: cur into pre and pre.next
            _next = cur.next
            cur.next = _next.next
            _next.next = pre.next
            pre.next = _next
            k +=1
        
        return fakehead.next
        
