# -*- coding:utf-8 -*-


# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        fake=ListNode(0)
        fake.next=head
        node=head
        pre=fake
        flag=False
        
        while node:   
            if node.val == val:
                flag=True
            else:
                if flag == True:
                    pre.next=node
                    flag=False
                pre=node
            node=node.next
            
        if flag == True:
            pre.next=None
    
        return fake.next
            
