# -*- coding:utf-8 -*-


# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
#
#
#
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
#
# Return the sum = 12 + 13 = 25.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = [0]
        
        def helper(root, _sum):
            
            if not root: return 
            
            _sum = _sum*10+root.val
            if not root.left and not root.right:
                res[0] += _sum
            
            if root.left:
                helper(root.left, _sum)
            if root.right:
                helper(root.right, _sum)
        
        helper(root, 0)
        return res[0]
            
