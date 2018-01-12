# -*- coding:utf-8 -*-


#
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
#
#
# Return a deep copy of the list.
#


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head: return None
        """
        # hash method
        
        _map = {}
        cur = head
        while cur:
            _map[cur] = RandomListNode(cur.label)
            cur = cur.next
        
        cur = head
        while cur:
            _map[cur].next = _map.get(cur.next) # get, because next or random can be None
            _map[cur].random = _map.get(cur.random)
            cur = cur.next
        
        return _map[head]
        """
        
        # 1->1'->2->2'->3->3'
        cur = head
        while cur:
            next = cur.next
            new = RandomListNode(cur.label)
            cur.next = new
            new.next = next
            cur = next
            
        cur = head
        while cur:
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next
        
        newHead = head.next
        cur1 = head
        cur2 = newHead
        while cur1:
            cur1.next = cur1.next.next
            if cur2.next: cur2.next = cur2.next.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        return newHead

