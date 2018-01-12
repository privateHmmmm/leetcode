# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummyHead = ListNode(0)
        cur = dummyHead
        
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2 or carry:
            num1, num2 = 0, 0
            if p1:
                num1 = p1.val
                p1 = p1.next
            if p2:
                num2 = p2.val
                p2 = p2.next
            _sum = num1 + num2 + carry
            newNode = ListNode(_sum % 10)
            carry = _sum / 10
            cur.next = newNode
            cur = newNode
        
        return dummyHead.next
             
