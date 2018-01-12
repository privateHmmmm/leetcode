# -*- coding:utf-8 -*-


#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
#
#
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if not root: return []
        
        res = []
        cur = []
        
        def robot(root, now):
            
            if not root: return
            
            now += root.val
            cur.append(root.val)
            
            if not root.left and not root.right and now == sum:
                res.append(copy.copy(cur))
        
            if root.left:
                robot(root.left, now)
            if root.right:
                robot(root.right, now)
            
            cur.pop()
            
        robot(root, 0)
        return res
            
