# -*- coding:utf-8 -*-


#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
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
        
        fakehead = ListNode(0)
        pre = fakehead; cur = head
        pre.next = cur
        flag = False
        
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
                flag = True
            else:
                if flag == True:
                    flag = False
                    pre.next = cur.next
                    cur = pre.next
                else:
                    pre = cur
                    cur = cur.next
        
        return fakehead.next 
        
