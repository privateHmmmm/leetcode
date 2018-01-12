# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
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
        
#         num1 = 0
#         l = l1
#         while l:
#             num1 = num1*10+l.val
#             l = l.next
        
#         num2 = 0
#         l = l2
#         while l:
#             num2 = num2*10+l.val
#             l = l.next
        
#         Sum = num1+num2
#         if Sum == 0:
#             return ListNode(0)
        
#         fakehead = ListNode(-1)
#         while Sum:
#             num = Sum%10
#             Sum = Sum/10
#             newNode=ListNode(num)
#             newNode.next = fakehead.next
#             fakehead.next=newNode
            
#         return fakehead.next

        num1 = 0
        while l1:
            num1 = num1*10+l1.val
            l1 = l1.next
            
        num2 = 0
        while l2:
            num2 = num2*10+l2.val
            l2 = l2.next
        
        _sum = num1+num2
        if _sum == 0: return ListNode(0)
        cur = None
        
        while _sum:
            num = _sum % 10
            _sum = _sum/10
            newNode = ListNode(num)
            newNode.next = cur
            cur = newNode
        
        return cur
        
