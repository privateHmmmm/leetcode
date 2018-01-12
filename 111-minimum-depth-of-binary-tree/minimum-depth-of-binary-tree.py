# -*- coding:utf-8 -*-


# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        """
                        10
                |                |
                3               18
           |         |      |         |
           2         (4)    13        14
                         |
                         9
        """
        
        if not root: return 0
        
        if not root.left or not root.right: 
            return max(self.minDepth(root.left), self.minDepth(root.right))+1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
