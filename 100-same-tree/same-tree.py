# -*- coding:utf-8 -*-


#
# Given two binary trees, write a function to check if they are the same or not.
#
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
#
#
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
#
#
#
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
#
#
#
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
#         def compare(p1, q1):
        
#             if (p1 and not q1) or (q1 and not p1):
#                 return False
                
#             if not p1 and not q1:
#                 return True
                
#             if p1.val != q1.val:
#                 return False
            
#             if compare(p1.left, q1.left) == False:
#                 return False
            
#             return compare(p1.right, q1.right)
    
        
        if (q == None and p == None):
            return True
        
        if (q != None and p != None and q.val == p.val):
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        
        return False
            
        
        
