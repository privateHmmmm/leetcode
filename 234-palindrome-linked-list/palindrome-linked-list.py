# -*- coding:utf-8 -*-


# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        def findmiddle(head):
            
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(head):
            
            pre = None
            while head:
                _next = head.next
                head.next = pre
                pre = head
                head = _next
                
            return pre
        
        if head == None or head.next == None: return True
        middle = findmiddle(head)
        middle.next = reverse(middle.next)
        
        p1, p2 = head, middle.next
        while p1 and p2:
            if p1.val != p2.val: return False
            p1=p1.next
            p2=p2.next
        return True
        
        
