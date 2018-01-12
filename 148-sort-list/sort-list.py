# -*- coding:utf-8 -*-


# Sort a linked list in O(n log n) time using constant space complexity.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        middle = self.getmiddle(head)
        _next = middle.next
        middle.next = None
        # print head.val, _next.val
        return self.merge(self.sortList(head), self.sortList(_next))
    
    def getmiddle(self, head):
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        
        fakehead = ListNode(0)
        cur = fakehead
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 == None: 
            cur.next = l2
        else:
            cur.next = l1
        
        return fakehead.next
            
