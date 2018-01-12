# -*- coding:utf-8 -*-


# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
#
# Input:
# 1->2->3
#
# Output:
# 1->2->4
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        fakehead = ListNode(0)
        fakehead.next = head
        
        i, j = fakehead, fakehead
        while i:
            if i.val != 9:
                j = i
            i = i.next
        
        j.val +=1
        j = j.next
        while j:
            j.val = 0
            j = j.next
        
        return fakehead if fakehead.val != 0 else head
        
