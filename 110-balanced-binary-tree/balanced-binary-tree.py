# -*- coding:utf-8 -*-


# Given a binary tree, determine if it is height-balanced.
#
#
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def height(root):
            
            if not root: return 0
            
            left = height(root.left)
            right = height(root.right)
            
            if left ==-1 or right == -1 or abs(left-right) > 1:
                return -1          # !!!
            
            return max(left, right) +1
        
        if not root: return True
        return height(root) != -1
            
