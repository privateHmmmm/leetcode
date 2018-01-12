# -*- coding:utf-8 -*-


# Sort a linked list using insertion sort.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
    
        helper = ListNode(-1)
        pre = helper # insert node between pre and pre.next
        cur = head
        
        # not the end of input list
        while cur != None:
            next = cur.next
            if pre != None and pre.next != None and pre.next.val >= cur.val:
                pre = helper
            
            # find the right place to insert
            while pre.next != None and pre.next.val < cur.val: 
				pre = pre.next
			
            cur.next = pre.next
            pre.next = cur
                
            #pre = helper
            cur = next
            
        return helper.next
    
    
    
