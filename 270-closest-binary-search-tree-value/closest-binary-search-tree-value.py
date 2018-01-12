# -*- coding:utf-8 -*-


#
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        self.res = root.val
        
        while root:
            self.res = root.val if abs(root.val-target) < abs(self.res-target) else self.res
            if root.val > target:
                root = root.left
            elif root.val == target:
                self.res = root.val
                break
            else:
                root = root.right
        
        return self.res
        
