# -*- coding:utf-8 -*-


#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#


from heapq import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        """
        # time: O(nlogk) k: len(lists), n: all nodes num of all lists
        
        hq = []
        
        for l in lists:
            if l: heappush(hq, (l.val, l))
        
        dummyHead = ListNode(0)
        cur = dummyHead
        while hq:
            node = heappop(hq)[1]
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(hq, (node.next.val, node.next))
        
        return dummyHead.next
        """
        
        
        
        
        
        
        
        
        
        def merge(l1, l2):
            
            dummyHead = ListNode(0)
            cur = dummyHead

            p1, p2 = l1, l2
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next

            if p1:  cur.next = p1 # more precise
            if p2:  cur.next = p2

            return dummyHead.next
        
        # time: T(k) = 2*T(k/2) + n (k: len(lists), n: max length of one list)
        def mergeSort(lists):
            
            if lists == []: return None
            if len(lists) == 1: return lists[0]
            
            mid = (0+len(lists)-1)/2
            return merge(mergeSort(lists[0:mid+1]), mergeSort(lists[mid+1:]))
        
        return mergeSort(lists)

        
        
        
#         def mergeSort(lists):
            
#             if not lists: return None
#             if len(lists) == 1: return lists[0]
            
#             mid = (0+len(lists)-1)/2
#             l1 = mergeSort(lists[0:mid+1])
#             l2 = mergeSort(lists[mid+1:])
#             return merge(l1, l2)
        
#         def merge(l1, l2):
            
#             fakehead = ListNode(0)
#             cur = fakehead
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     cur.next = l1
#                     l1 = l1.next
#                 else:
#                     cur.next = l2
#                     l2 = l2.next
#                 cur = cur.next
                
#             if l1 == None:
#                 cur.next = l2
#             else:
#                 cur.next = l1
                
#             return fakehead.next
            
#         return mergeSort(lists)
            
