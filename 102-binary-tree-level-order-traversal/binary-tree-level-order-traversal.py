# -*- coding:utf-8 -*-


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        
        stack = [root]
        res = []
        
        while stack not in [None, [], [None]]:
            lens=len(stack)
            i = 0
            tmp_list = []
            while i < lens:
                node = stack.pop(0)
                tmp_list.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    
                i += 1
            
            res.append(tmp_list)
        
        return res
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
