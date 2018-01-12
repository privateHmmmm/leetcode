# -*- coding:utf-8 -*-


#
# Given a binary tree, find the length of the longest consecutive sequence path.
#
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
#
#
# For example,
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# Longest consecutive sequence path is 3-4-5, so return 3. 
#
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
#
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max_lens = 0
        
        def helper(root, lens):
            
            if not root: return 

            self.max_lens = max(self.max_lens, lens)
            
            if root.left:
                tmp = lens + 1 if root.left.val == root.val+1 else 1
                helper(root.left, tmp)
                
            if root.right:
                tmp = lens + 1 if root.right.val == root.val+1 else 1
                helper(root.right, tmp)
            
        if not root: return 0
        helper(root, 1)
        return self.max_lens
        
