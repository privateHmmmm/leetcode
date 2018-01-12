# -*- coding:utf-8 -*-


# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
# But the following [1,2,2,null,3,null,3]  is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def robot(root1, root2):
            
            if not root1:
                return not root2
            elif not root2:
                return False
        
            if root1.val != root2.val: return False
            return robot(root1.left, root2.right) and robot(root1.right, root2.left)
        
        if not root: return True
        return robot(root.left, root.right)
